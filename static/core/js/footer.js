
$(document).ready(function() {


    // navbar menu toggle
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


    // vavle control
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

    // close button modals
    (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
        const $target = $close.closest('.modal');
    
        $close.addEventListener('click', () => {
          $target.classList.remove('is-active');
        });
      });

});


