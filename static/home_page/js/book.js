$(document).on("click", "#add-book", get_book);//on to link with created and don't created element


function get_book() {
    const data = $(this).data('book');
    console.log(data);
    $.ajax({
        url: 'order_books',
        type: 'post',
        data: JSON.stringify(data),
        success: function (data) {
            alert(data);
        }
    })
    ;
}


