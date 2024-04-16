# pinephone-max30102
Pulse Oximeter and
Heart-Rate sensor board for PinePhone

## What it is:
Sensor board attaches I2C interface exposed on the pogo pin expansion port in the back of the PinePhone.  
Interface is numbered as i2c-3 in multiple operating systems.
To expose the power and interfaces in the pogo pins you can use my other design "PinePhone flex breakout board".   

<a href="https://github.com/jnavarro7/pinephone_flex_breakout_board" title="PinePhoone flex breakout board">PinePhone flex breakout board source</a>

<a href="https://pine64.com/product/pinephone-flex-break-out-board/" title="Buy the PinePhoone flex breakout board from Pine64">Buy the PinePhone flex breakout board from Pine64</a>

## Sensor


[max30102 datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/max30102.pdf)


![max30102 system diagram](/support_files/images/system_diagram.JPG)


## Component placement

In progress . . .

U4 Is currently placed in the bottom of the board as user will use the index finger to place it on top of this sensor. 

![component placement](/support_files/images/board.JPG)


## License

Released under the Creative Commons Attribution 4.0 License
https://creativecommons.org/licenses/by/4.0/