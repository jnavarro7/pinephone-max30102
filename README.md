# pinephone-max30102
Pulse Oximeter and
Heart-Rate sensor board for PinePhone

## What it is:
Sensor board that sports the MAX30102 pulse oximeter and heart-rate sensor. The board attaches to the I2C interface exposed on the pogo pin expansion port in the back of the PinePhone.  
Interface is numbered as i2c-3 in multiple operating systems.
To expose the power and interfaces in the pogo pins you can use my other design "PinePhone flex breakout board". 


<a href="https://github.com/jnavarro7/pinephone_flex_breakout_board" title="PinePhoone flex breakout board">PinePhone flex breakout board source</a>

<a href="https://pine64.com/product/pinephone-flex-break-out-board/" title="Buy the PinePhoone flex breakout board from Pine64">Buy the PinePhone flex breakout board from Pine64</a>

## Block Diagram

![block_diagram](/support_files/images/block_diagram.JPG)


## Assembly mockup
![pinephone_assembly](/support_files/images/pinephone_assembly_mockup.jpg)
## Sensor


[max30102 datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/max30102.pdf)


![max30102 system diagram](/support_files/images/system_diagram.JPG)

### I2C address 
    Write address = 0xAE 
    Read address = 0xAF

## Component placement

Revision 1 placement completed.

U4 Is currently placed in the bottom of the board as user will use the index finger to place it on top of this sensor. 

![board top](/support_files/images/board.JPG)

![board bottom](/support_files/images/board_bottom.JPG)

## EDA

Designed in DipTrace 4.3

## License

Released under the Creative Commons Attribution 4.0 License
https://creativecommons.org/licenses/by/4.0/