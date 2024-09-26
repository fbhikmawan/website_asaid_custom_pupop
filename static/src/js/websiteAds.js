/** @odoo-module **/

import { registry } from '@web/core/registry';

function openModal() {
    $('#modalAds').css('display', 'flex');
}

function closeModal() {
    $('#modalAds').css('display', 'none');
}

$(document).ready(function() {
    openModal(); // Automatically open the modal on page load

    // Bind the close event to the close button
    $('.website_asaid_custom_popup_close').on('click', function(event) {
        event.preventDefault();
        closeModal();
    });
});


// Register the module to ensure it's loaded
registry.category('modalAds').add('modal', {
    openModal,
    closeModal,
});