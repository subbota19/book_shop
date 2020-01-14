$(init);

function init() {
    $('#add-book').bind('click', get_book)

}

function get_book() {
    const data = $(this).data('book')
    console.log(data)
    $.ajax({
        url: 'books_image',
        type: 'post',
        data: JSON.stringify(data),
        success: function (data) {
            alert(data)
        }
    })
    ;
}
