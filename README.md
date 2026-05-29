# DAC
Welcome to the repo for DAC!  
  
DAC is a Discord bot designed to be a digital helper for TTRPGs.  
DAC stands for Dice And Cart, and is affectionately called "dacca".  
[View the GitHub Project board here](https://github.com/users/Jynx972/projects/3)

[View the DAC wiki for all DAC-Related info!](https://github.com/Jynx972/dacca-discord/wiki)

## Help Message:
Sending DAC- help into a channel that DAC can see will print the following message:  
  
Thankyou for using DAC!  
  
Currently I have two main features, a dice roller and cart management system,  
  
To use the dice roller, simply type: `DAC- roll (x)d(y) (z)` and I will roll an amount of `y` sided dice equal to `x` and apply modifier `z` to each roll.  
You may also add `kh(i)` to the command, to only display the highest `i` results.  
The roller can also do GENESYS/SWRPG rolls by using `DAC- roll sw` then adding the dice you want to roll. `b`=blue `bk`=black `g`=green `p`=purple `y`=yellow `r`=red `f` or `w`=force die.  
  
To use the cart system, see commands below:  
    \- `list` will display the currently loaded cart  
    \- `load (cart_name)` will load cart `cart_name` into the system (names cannot have spaces)  
    \- `add  (item/carry) (name) (item_weight/carry_capacity) (item_amount)` will add either an item or carrier to the current cart (note: amount is only for items)  
    \- `del (item/carry) (x)` will delete item or carrier with index `x` from the system (use `list` to get the index number)  
    \- `save (cart_name)` will save the current cart as `cart_name`. If you do not specify a name, it will save as the name you used when loading (or 'placeholder' if no cart was loaded)  
    \- `show` will show all the carts that can be loaded into the system  
