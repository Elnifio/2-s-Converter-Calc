# 2's Complement Converter Calculator

This is a calculator that converts numbers from one base to another base in **"2's Complement"**.

First download all code in src folder and put them into a local folder, and open Terminal / command line / PowerShell, `cd` to the folder that stores these code.

Then, input `python main.py` or `python3 main.py` as appropriate. `main.py` should be running after this command.

In Terminal, `main.py` would ask you to enter requirement for conversion, 
in the format of `$INPUT to $OUTPUT`.
For instance, if you want to convert binary to hexadecimal, enter `bin to 16`.

All available base identifier are listed below:
1. Binary: `["bin", "binary", "bit", "bits", "b", "2", "two"]`
2. Octal: `["oct", "octo", "octal", "o", "8", "eight"]`
3. Decimal: `["dec", "decimal", "d", "10", "ten"]`
4. Hexadecimal: `["hex", "hexadecimal", "h", "16", "sixteen"]`

All of these identifiers are "identifiable", or equivalent. 
i.e., if you want to convert binary to hexadecimal, 
all of the following inputs are equivalent:
* bin to 16
* 2 to 16
* 2 to hex
* binary to h
* bit to sixteen

After you have entered the requirements,
the program would then ask you to enter the input number
that you want to convert, in the format specified below:
* Binary: Input should be comprised only of 0 and 1, 
note the first digit represents the "Complement digit"
* Octal: Input should begin with 0, and be comprised only of 0 - 7.
* Decimal: Normal decimal representations
* Hexadecimal: Input should start with 0x, and comprised only of 0-9 and A-F,
not case sensitive. 

After you have entered input, hit `Return` or `Enter`.
The output will show automatically,
also using "2's Complement".
* * *
### Flaws & TODOs
- [ ] No Visual Representations. This might be added in the future.
- [ ] Does Not Support Octal. This should be added soon.
- [ ] Does Not Support Digital Representation. ~~I don't know when this feature will be added:)~~

~~and as a non-native speaker, I mistakenly spelled "Complementary" as "Complimentary" LOL. This bug would be fixed soon.~~
