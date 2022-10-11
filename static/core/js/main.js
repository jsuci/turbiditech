

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


    // modal pop up
    // Functions to open and close a modal
    function openModal($el) {
        $el.classList.add('is-active');
    }
    
    function closeModal($el) {
        $el.classList.remove('is-active');
    }
    
    function closeAllModals() {
        (document.querySelectorAll('.modal') || []).forEach(($modal) => {
            closeModal($modal);
        });
    }
    
    // Add a click event on buttons to open a specific modal
    (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
        const modal = $trigger.dataset.target;
        const $target = document.getElementById(modal);
    
        $trigger.addEventListener('click', () => {
        openModal($target);
        });
    });
    
    // Add a click event on various child elements to close the parent modal
    // remove .modal-background
    (document.querySelectorAll('.modal-close, .modal-card-head .delete, footer .button') || []).forEach(($close) => {
        const $target = $close.closest('.modal');
    
        $close.addEventListener('click', () => {
            closeModal($target);
        });
    });
    
    // Add a keyboard event to close all modals
    document.addEventListener('keydown', (event) => {
        const e = event || window.event;
    
        if (e.key === 27) { // Escape key
        closeAllModals();
        }
    });

});
