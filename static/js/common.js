// plugin for visible
$.fn.visible = function() {
    return $.expr.filters.visible(this[0]);
};


$(function(){

	// form ajax

	var req;

	if( $('form').data('use-ajax') ){
		
	    $('form').bind("submit", function(e) {
			
	        e.stopPropagation();
				

	        var form = $(this);        
	        var submit_btn = form.find('*[type="submit"]');


	        req = $.ajax({
	            url: form.attr('action')+'?use-ajax=true',
	            type: form.attr('method'),
	            data: form.serialize(),
	            timeout: 50000,
	            beforeSend: function(xhr, settings) {
	                // submit_btn
	                // 	.attr('type', '')
	                // 	.removeClass('btn-primary')
	                // 	.addClass('btn-danger')
	                // 	.on('click', abort_event)
	                // 	.after($('<div />', {class: 'loading'}))
	                // 	.text('中止')
	                $('.errorlist').remove()
	            },
	            complete: function(xhr, textStatus) {
	                // submit_btn
	                // 	.attr('type', 'submit')
	                // 	.removeClass('btn-danger')
	                // 	.addClass('btn-primary')
	                // 	.off('click')
	                // 	.text('確定')
	                // $('.loading').remove()
	            },
	            success: function(result, textStatus, xhr) {
	            	console.log(result)
					var json = $.parseJSON(result);             
					if( json.result ){
						window.location.href = json.redirect_to
					}else{
						$.each(json.errors, function(key) { 
							val = json.errors[key]
							errors = $('<ul />', {class: "errorlist"})
							$.each(val, function(key) { 
								errors.append($('<li />', {text: val[key]}))
							})
							$('#id_'+key).before(errors)
						})
					}
	            },
	            error: function(xhr, textStatus, error) {
					console.log('error')					
			        console.log(error)
			        console.log(xhr.statusText)
	            }
	        });

	        // var abort_event = function(){
	        // 	req.abort()
	        // }

			return false;
		});
	}
})    
