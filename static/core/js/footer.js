
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


    // close button modals
    (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
        const $target = $close.closest('.modal');
    
        $close.addEventListener('click', () => {
          $target.classList.remove('is-active');
        });
      });


    // display water status everytime page reload

    const allWaterStat = document.querySelectorAll('.water-stat');
    const recordsUrl = 'http://127.0.0.1:8000/api/turbidity-records/'
    
    for (const eachWaterStat of allWaterStat) {
        device_id = eachWaterStat.getAttribute('data-id');
        
        fetch(`${recordsUrl}${device_id}`, {
            method: 'GET',
        })
        .then((response) => response.json())
        .then((data) => {
            const latestRecord = data[data.length-1]

            if (latestRecord != undefined) {

                console.log(latestRecord);

            } else {
                console.log('No records yet.');
            }
        });
    }

});


