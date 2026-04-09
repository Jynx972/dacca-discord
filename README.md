# DAC
Welcome to the repo for DAC!  
  
DAC is a Discord bot designed to be a digital helper for TTRPGs.  
DAC stands for Dice And Cart, and is affectionately called "dacca".  

## History
He was born out of a need to replace an ageing piece of A4 paper that my D&D party was using to track all the items we stored in our cart.  
I used my skills as an amateur python developer to produce a rudimentary terminal program to track items against carrying capacity.  
Eventually, I wanted the party to have access to this information, so I looked into the "discord" python package and API to make DAC able to send messages to our D&D group's Discord Server.  

## How to Run
DAC was developed for UNIX operating systems, and is currently untested on Windows based systems.  
DAC is also entirely self-hosted, therefore in order to use him you will need to create your own application in the [Discord Developer Portal](https://discord.com/developers/home).  
You will need to copy the token generated for your application and paste it as the first line in the "tokenfile" file.  
You should then be able to invite your bot to your desired server (provided you have the permissions to) and run the "dac_main.py" file from a terminal with Python 3.12.  

## Help Message:
Sending DAC- help into a channel that DAC can see will print the following message:  
  
Thankyou for using DAC!  
  
Currently I have two main features, a dice roller and cart management system,  
  
To use the dice roller, simply type: `DAC- roll (x)d(y) (z)` and I will roll an amount of `y` sided dice equal to `x` and apply modifier `z` to each roll.  
You may also add `kh(i)` to the command, to only display the highest `i` results.  
The roller can also do swrpg rolls by using `DAC- roll sw` then adding the dice you want to roll. `b`=blue `bk`=black `g`=green `p`=purple `y`=yellow `r`=red `f` or `w`=force die.  
  
To use the cart system, see commands below:  
    \- `list` will display the currently loaded cart  
    \- `load (cart_name)` will load cart `cart_name` into the system (names cannot have spaces)  
    \- `add  (item/carry) (name) (item_weight/carry_capacity) (item_amount)` will add either an item or carrier to the current cart (note: amount is only for items)  
    \- `del (item/carry) (x)` will delete item or carrier with index `x` from the system (use `list` to get the index number)  
    \- `save (cart_name)` will save the current cart as `cart_name`. If you do not specify a name, it will save as the name you used when loading (or 'placeholder' if no cart was loaded)  
    \- `show` will show all the carts that can be loaded into the system  