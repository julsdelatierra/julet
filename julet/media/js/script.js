$(document).ready(function(){
    $('.gift').click(function(){
        row = $(this).parent();
        text = $(row.children()[1]);
        if($(this).attr('checked')!=undefined){
            var answer = confirm("¿Aceptas darnos ese regalo?");
            if(answer){
                $(this).attr('disabled','true');
                $.get('/marcar/regalo?id='+$(this).val(),function(){
                    text.css('text-decoration','line-through');
                });
            }
            else{
                $(this).attr('checked',false);
            }
        }
    });
    if($('#site_info')!=undefined){
        $('#site_info').hide();
    }
    if($('#site_gifts')!=undefined){
        $('#site_gifts').hide();
    }
    
    $('#index_button').click(function(){
        $('#site_info').slideUp('slow');
        $('#site_gifts').slideUp('slow',function(){
            $('#site_index').slideDown('slow');
        });
        return false;
    });
    $('#info_button').click(function(){
        $('#site_index').slideUp('slow');
        $('#site_gifts').slideUp('slow',function(){
            $('#site_info').slideDown('slow');
        });
        return false;
    });
    $('#gifts_button').click(function(){
        $('#site_info').slideUp('slow');
        $('#site_index').slideUp('slow',function(){
            $('#site_gifts').slideDown('slow');
        });
        return false;
    });
});
