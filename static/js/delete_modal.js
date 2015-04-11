$(function() {

    $('.fancybox-photo').fancybox({
        // openEffect : 'none',
        // closeEffect  : 'none',
        prevEffect : 'none',
        nextEffect : 'none'
    });

    $('.btn-confirm-delete-close').on('click', function(){
        $.fancybox.close()
    })
    $('.btn-confirm-delete').on('click', function(){
        $("#confirm-delete").find('form').attr('action', $(this).data('url'))
    })
    $('.btn-confirm-delete').fancybox({
        modal: true,
        closeBtn: true
    })
});
