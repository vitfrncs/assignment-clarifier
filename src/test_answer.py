from main import extract_answer


def test_extract_answer():
    data = {
        "message": {
            "role": "assistant",
            "content": "  Objetivo: elaborar um relatório.  "
        }
    }

    result = extract_answer(data)

    assert result == "Objetivo: elaborar um relatório."

    print("Passou: extração de texto válido e remoção de espaços")


def test_extract_answer_invalid_responses():
    cases = [
        ("Resposta em lista", []),
        ("Mensagem ausente", {}),
        ("Mensagem com tipo incorreto", {"message": "texto"}),
        ("Conteúdo ausente", {"message": {}}),
        ("Conteúdo numérico", {"message": {"content": 123}}),
        ("Conteúdo vazio", {"message": {"content": ""}}),
        ("Conteúdo com espaços", {"message": {"content": "   "}}),
    ]

    for description, data in cases:
        try:
            extract_answer(data)
        except ValueError:
            print(f"Passou: {description}")
        else:
            raise AssertionError(
                f"Era esperado um ValueError: {description}"
            )


if __name__ == "__main__":
    test_extract_answer()
    test_extract_answer_invalid_responses()
    print("\nTodos os testes de extração passaram.")