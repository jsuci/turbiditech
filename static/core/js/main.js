
// navbar menu toggle
$(document).ready(function() {
//jquery for toggle sub menus
    $('.sub-btn').click(function() {
        $(this).next('.sub-menu').slideToggle();
        $(this).find('.dropdown').toggleClass('rotate');
    });
    //jquery for expand and collapse the sidebar
    $('.menu-btn').click(function() {
        $('.side-bar').addClass('active');
        $('.menu-btn').css("visibility", "hidden");
    });
    $('.close-btn').click(function() {
        $('.side-bar').removeClass('active');
        $('.menu-btn').css("visibility", "visible");
    });
});

// valve control toggle
$(document).ready(function() {
    $('input[type=checkbox]').change(function() {
        
        if (this.checked == true) {
            console.log('valve_status set to `on`', 'device: ', this.id)
            console.log('turbidity set to `clean`', 'device: ', this.id)
        } else {
            console.log('valve_status set to `off`', 'device: ', this.id)
            console.log('turbidity set to `dirty`', 'device: ', this.id)
        }
        // $.post(`/update-device/${this.id}`, {
        //     id: '{{workexperiance.id}}', 
        //     isworking: this.checked, 
        //     csrfmiddlewaretoken: '{{ csrf_token }}' 
        // });
    });
});