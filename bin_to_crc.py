def calculate_crc16(data):
    crc = 0xFFFF

    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1

    return crc.to_bytes(2, byteorder='big')

def main():
    input_file = 'board1_300_3c.bin'

    with open(input_file, 'rb') as f:
        file_data = f.read()

    # Ignore the last 2 bytes of the file
    data_to_process = file_data[:-2]

    crc_result = calculate_crc16(data_to_process)
    print("CRC-16 Modbus:", crc_result.hex()[2:],crc_result.hex()[:2])

if __name__ == "__main__":
    main()





