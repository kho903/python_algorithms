dataset = ["aasdfasdf", "dsfadf", "sadfasdfiwsfghasd", "fdsajfkasdf", "fsdjmaksd", "dsmjkfasd", "jiahmfdkasdf",
           "dfnansfmsadmfasmdfas", "adsmfsad", "dsfas", 'disoff']

m_count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == 'm':
            m_count += 1

print(m_count)
