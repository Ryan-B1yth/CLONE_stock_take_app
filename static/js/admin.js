$('.toast').toast('show');

function firstDropdown() {
    $(this).next('div').slideToggle()
}

function secondDropdown() {
    $(this).parent().children('div').slideToggle()
}

function thirdDropdown() {
    $(this).next('div').slideToggle()
}

$(document).ready( function() {
    $('.parts-dropdown').slideToggle()
    $('.products-dropdown').slideToggle()
    $('.stock-list').slideToggle()

    $('.first').click( firstDropdown )
    $('.second').click( secondDropdown )
    $('.third').click( thirdDropdown )
})