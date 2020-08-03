# Contributing

## Contributions welcome!
All contributions are welcomed, whether it is just one aircraft or an entire fleet.

If you are unsure where to start, please look at the issues labelled 'help wanted'.

If you would like to request the addition of an aircraft to this repository, please open an issue.

Please follow the contribution guidelines below:

## Contribution guidelines
### The repository
* Where feasible, please create a pull request for one aircraft (range) at a time, e.g. B732 - B739.
* It could be that multiple aircraft can use the same icon, for example when only internals are different (e.g. cockpit, engine). Do not include the icon twice, but add an entry in the 'duplicates.json' file.
    * The format is `"model ICAO code": "icon to use ICAO code"`.
* If an icon is not created or missing for any reason but there is an icon availabile that closely resembles the aircraft model, add an entry in the 'placeholders.json' file.
    * The format is `"model ICAO code": "icon to use ICAO code"`.
    * It is always preferable to have a unique icon instead of a placeholder.
* The main focus lies on commercial and general aviation aircraft, but military aircraft could be added too.
* Please do not use copyrighted work.

### Icon
* The canvas used is 250x100mm. Please keep the size/aspect ratio the same.
* The icon should consist of a solid black surface following the profile of the aircraft, with cutouts for windows only. No internals should be drawn.
* Depict the aircraft from the side, as if they were parked/taxiing. That means: Gear extended, flaps retracted, wingtips folded up, rotor stationary, etc.
* The nose of the depicted aircraft should point left.
* If multiple models fit the same ICAO identifier, use the most recently issued model. 
* Aircraft are not to scale compared to each other. Instead, use as much of the frame as possible while keeping a little margin, and not distorting the proportions of the model.
* For uniformity, the 'ground level' the aircraft are standing on should be 10mm from the bottom.

### The file
* Please use the aircraft codes as specified in the ICAO8643 document as filename convention.
* The filenames use capital letters.
* Run your svg file through an svg optimizer, and please ensure the image looks the same afterwards.
