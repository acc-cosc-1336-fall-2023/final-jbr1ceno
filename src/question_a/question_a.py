#write functions here, don't add input('') statements here!


def create_multiplication_table(max_valueR, max_valueC):
    m_table = []

    for r in range(1, max_valueR + 1):
        row = []

        for c in range(1, max_valueC + 1):
            row.append(r*c)

        m_table.append(row)

    return m_table

def display_multiplication_table(m_table):

    #stringEmpty = " "
    #print(m_table)
    for r in range(len(m_table)):
        #for c in range(len(m_table[r])):
            print(*m_table[r], " ")