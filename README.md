# ASAid Custom Popup

## Overview

ASAid Custom Popup is a custom Odoo 17 module that allows you to display custom popups as modals on various website pages, including blog posts, product items, events, and others. The modal appearance can be toggled using Website Builder options.

## Features

- Display custom popups on specific website pages
- Toggle popup visibility for each page through the Website Builder
- Customizable popup content
- Automatic popup display on page load
- Easy integration with existing Odoo websites

## Installation

1. Clone this repository into your Odoo addons directory:
   ```
   git clone https://github.com/fbhikmawan/website_asaid_custom_pupop.git
   ```

2. Update your Odoo addons list:
   - Go to Apps menu
   - Click on "Update Apps List"

3. Install the module:
   - Search for "ASAid Custom Popup" in the Apps menu
   - Click "Install"

## Configuration

1. Go to Website > Pages in the Odoo backend
2. Select the page where you want to display the popup
3. In the "Publish" tab, you'll find a new option "Show Modal"
4. Toggle the "Show Modal" option to enable/disable the popup for that specific page

## Usage

Once installed and configured, the module will automatically display the popup on the selected pages when a visitor loads the page.

To customize the popup content:

1. Navigate to `views/modal_template.xml`
2. Modify the content within the `<div class="modal-content">` tag

## Customization

You can further customize the popup's appearance by modifying the SCSS file:

- Edit `static/src/scss/websiteAds.scss` to change the styling of the popup

To modify the behavior of the popup, you can edit the JavaScript file:

- Edit `static/src/js/websiteAds.js` to change how the popup opens, closes, or behaves

## Dependencies

This module depends on:
- `base`
- `website`

## Contributing

Contributions to improve ASAid Custom Popup are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a new Pull Request

## Support

For support, please contact ASAid Group Investment at support@asaidgroup.com or visit our website at https://www.asaidgroup.com.

## License

This module is licensed under the LGPL-3.0 License. See the [LICENSE](LICENSE) file for details.

## Authors

- ASAid Group Investment
- Fatchul Bari Hikmawan


---
For more information about Odoo development, visit the [official Odoo documentation](https://www.odoo.com/documentation/17.0/).