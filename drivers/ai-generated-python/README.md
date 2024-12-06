# AI generated test driver

## The prompt: 

    From the attached MAX30102 data sheet generate a sensor test driver using python that will be run on a PinePhone with Manjaro OS over the I2C interface which is numbered as i2c-3, use 0xAE as the write address and 0xAF as the read address, give instructions on how to cover for any dependency.  


The genated driver: 

[ai-generated-driver.py](ai-generated-driver.py)

## MAX30102 Driver Setup Instructions

## Dependencies

1. **Install Required Libraries**
   - Ensure that you have Python 3 installed.
   - Install the `smbus2` library using `pip`:
     ```bash
     sudo pacman -S python-pip
     pip install smbus2
     ```

2. **Enable I2C on PinePhone**
   - Check if the `i2c-dev` module is loaded:
     ```bash
     lsmod | grep i2c
     ```
   - If the module is not loaded, load it with:
     ```bash
     sudo modprobe i2c-dev
     ```

3. **Verify I2C Bus**
   - Install the `i2c-tools` package to check your I2C bus:
     ```bash
     sudo pacman -S i2c-tools
     ```
   - Use `i2cdetect` to confirm the sensor is detected on bus `i2c-3`:
     ```bash
     sudo i2cdetect -y 3
     ```
   - You should see the sensor address (0x57 when shifted to 7-bit) listed in the output.

4. **Run the Script**
   - After completing the setup, execute the Python script:
     ```bash
     python3 max30102_driver.py
     ```

---

## Troubleshooting
- If the sensor is not detected, double-check the wiring and I2C address in the script.
- Ensure that the I2C interface on your PinePhone is enabled.

---

## Attribution
Portions of this project include code generated with AI assistance from OpenAI's ChatGPT. The original source for the MAX30102 implementation details is from the MAX30102 datasheet provided by Maxim Integrated.

## License
This project is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).