// plugin for visible
$.fn.visible = function() {
    return $.expr.filters.visible(this[0]);
};

$(function(){

	// form ajax
	if( $('form').data('validation') ){
		
	    $('form').bind("submit", function(e) {
	        e.stopPropagation();

	        var form = $(this);        
	        var button = form.find('button');

	        $.ajax({
	            url: form.attr('action')+'?validation=true',
	            type: form.attr('method'),
	            data: form.serialize(),
	            timeout: 10000,
	            beforeSend: function(xhr, settings) {
	                button.attr('disabled', true);
	                $('.errorlist').remove()
	            },
	            complete: function(xhr, textStatus) {
	                button.attr('disabled', false);
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
	            
	            // 通信失敗時の処理
	            error: function(xhr, textStatus, error) {
					console.log('error')					
			        console.log(error)
			        console.log(xhr.statusText)
	            }
	        });
			return false;
		});
	}
})    
