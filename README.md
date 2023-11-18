# Automatic-1111 Scripts

A collection of scripts to extend the functionality of [Automatic-1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

## Installation

1. Copy the contents of the script you want to use into a new file in the `scripts` folder of your webui installation.
2. Remove the `sys.path.append("automatic-1111")` line from the script. This is only needed for development (see below)

## Development

1. Clone this repository.
2. Run the following command to bootstrap the project:
   ```bash
   sh setup.sh
   ```
3. Create your new script in the root of this project.
4. For type hints to work in your new script, you need to add this line to the top of your script: `sys.path.append("automatic-1111")`.