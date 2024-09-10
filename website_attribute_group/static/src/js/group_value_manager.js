$("[group-id]").on('click', function(ev){
    var group_id = $(this).attr('group-id')
    if (group_id !== 'none'){
        $(".js_attribute_value[group-value="+group_id+"]").css('display', 'inline-block')
        $(".js_attribute_value[group-value="+group_id+"] input[default-selected='true']").prop('checked', 'checked');
        $(".group-value-name[group-value="+group_id+"]").css('display', 'flex')
    }else{
        $("ul[data-attribute_id=" + $(this).attr('attribute-id') + "] .js_attribute_value[group-value="+group_id+"] input").prop('checked', 'checked');
    }
    $("ul[data-attribute_id=" + $(this).attr('attribute-id') + "] li.js_attribute_value:not([group-value=" + group_id + "])").css('display', 'none')
    $(".group-names[attribute-id=" + $(this).attr('attribute-id') + "] .group-value-name:not([group-value=" + group_id + "])").css('display', 'none')
});