
$(document).ready(function(){

    $('.js-fancybox').fancybox({
        // openEffect : 'none',
        // closeEffect    : 'none',
        prevEffect : 'none',
        nextEffect : 'none'
    });

    
    $('.js-slider').slick({
        // lazyLoad: 'ondemand',
        infinite: false,
        slidesToShow: 1,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 500,
                settings: {
                    slidesToShow: 1,
                }
            },
            {
                breakpoint: 700,
                settings: {
                    slidesToShow: 2,
                }
            },
            {
                breakpoint: 900,
                settings: {
                    slidesToShow: 3,
                }
            },
            {
                breakpoint: 1100,
                settings: {
                    slidesToShow: 4,
                }
            },
            {
                breakpoint: 99999,
                settings: {
                    slidesToShow: 5,
                }
            }

        ]
    });


    $('.js-delete-button').fancybox({
        modal:true,
    })

    $(".js-delete-button").on('click',function(){
        $('#delete-target').html($(this).data('delete-target'))
        $('#delete-form').attr('action', $(this).data('target-url'))
        // return false
    })

    $('.js-confirm-delete-close').on('click',function(){
        $.fancybox.close()
        return false
    })

    $('.js-confirm-delete').on('click', function(){
        $("#confirm-delete").find('form').attr('action', $(this).data('url'))
    }).fancybox({
        modal: true,
        closeBtn: true
    })

})
