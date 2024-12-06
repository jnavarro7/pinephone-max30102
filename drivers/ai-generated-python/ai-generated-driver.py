import smbus2
import time

# I2C settings
I2C_BUS = 3  # i2c-3
WRITE_ADDR = 0xAE >> 1  # Shift for 7-bit address
READ_ADDR = 0xAF >> 1  # Shift for 7-bit address

# MAX30102 Registers
REG_INTR_STATUS_1 = 0x00
REG_INTR_STATUS_2 = 0x01
REG_INTR_ENABLE_1 = 0x02
REG_INTR_ENABLE_2 = 0x03
REG_FIFO_WR_PTR = 0x04
REG_FIFO_RD_PTR = 0x06
REG_FIFO_DATA = 0x07
REG_MODE_CONFIG = 0x09
REG_SPO2_CONFIG = 0x0A
REG_LED1_PA = 0x0C  # Red LED
REG_LED2_PA = 0x0D  # IR LED

# Initialize SMBus
bus = smbus2.SMBus(I2C_BUS)

def write_register(register, value):
    """Write a single byte to a register."""
    bus.write_byte_data(WRITE_ADDR, register, value)

def read_register(register):
    """Read a single byte from a register."""
    return bus.read_byte_data(READ_ADDR, register)

def read_fifo():
    """Read data from the FIFO."""
    raw_data = bus.read_i2c_block_data(READ_ADDR, REG_FIFO_DATA, 6)
    red = (raw_data[0] << 16) | (raw_data[1] << 8) | raw_data[2]
    ir = (raw_data[3] << 16) | (raw_data[4] << 8) | raw_data[5]
    return red, ir

def reset_fifo():
    """Reset FIFO pointers."""
    write_register(REG_FIFO_WR_PTR, 0x00)
    write_register(REG_FIFO_RD_PTR, 0x00)

def initialize_sensor():
    """Initialize the MAX30102 sensor."""
    write_register(REG_INTR_ENABLE_1, 0xC0)  # Enable A_FULL and PPG_RDY interrupts
    write_register(REG_INTR_ENABLE_2, 0x00)  # Disable other interrupts
    write_register(REG_MODE_CONFIG, 0x03)  # SpO2 mode
    write_register(REG_SPO2_CONFIG, 0x27)  # SPO2 settings: 411us, 100sps, full scale
    write_register(REG_LED1_PA, 0x24)  # Set Red LED current
    write_register(REG_LED2_PA, 0x24)  # Set IR LED current
    reset_fifo()

def main():
    """Main loop to read and display data."""
    initialize_sensor()
    print("Sensor initialized. Reading data...")
    try:
        while True:
            red, ir = read_fifo()
            print(f"Red: {red}, IR: {ir}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        bus.close()

if __name__ == "__main__":
    main()
