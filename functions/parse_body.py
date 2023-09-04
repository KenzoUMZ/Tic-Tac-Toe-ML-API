def parse_body(body_text):
    rows = body_text.split("\n")
    result = []

    # Assume the first row contains the headers for 'board' and 'resultado'
    headers = rows[0].split(",")
    board_index = headers.index("board")
    resultado_index = headers.index("resultado")

    for row in rows[1:]:
        values = row.split(",")
        board = values[board_index].split()  # Split the 'board' values into a list if needed
        resultado = values[resultado_index]
        result.append({"board": board, "resultado": resultado})

    return result
