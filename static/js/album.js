$(function() {

	$('.delete-button').fancybox({
	    modal:true,
	})

	$(".delete-button").on('click',function(){
    	$('#delete-target').html($(this).data('delete-target'))
    	$('#delete-form').attr('action', $(this).data('target-url'))
    	// return false
	})

	$('.confirm-delete-close').on('click',function(){
		$.fancybox.close()
		return false
	})
});
