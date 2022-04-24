console.log($('.user-row')[0])

$('.user-row').each( function() {
    $(this).click( () => {
        console.log($(this).index()) 
        console.log($('.products-dropdown')[$(this).index()])
    })})
