
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


    // display dashboard
    async function displayDashboard() {
        const recordsAPIURL = 'http://127.0.0.1:8000/api/turbidity-records/'
        const recordsURL = 'http://127.0.0.1:8000/turbidity-records/'
        const addDeviceURL = 'http://127.0.0.1:8000/add-device/'


        fetch(recordsAPIURL)
        .then((response) => response.json())
        .then((data) => {
            const boxContainer = document.querySelector('#box-container');

            if (data != false) {
                for (const record of data) {
                    const deviceName = record['device_name']
                    const deviceID = record['device_id']
                    const location = record['location']
                    const viewRecordsURL = recordsURL + record['id']
                    const latestrecord = record['records'][record['records'].length - 1]
                    const waterCleanHTML = `<td class="has-text-success has-text-right"><span>clean</span></td>`
                    const waterDirtyHTML = `<td class="has-text-white has-background-danger has-text-right"><span>dirty</span></td>`
                    const valveOffHTML = `<td><input class="toggle" data-id="${deviceID}" type="checkbox"/></td>`
                    const valveOnHTML = `<td><input class="toggle" data-id="${deviceID}" type="checkbox" checked/></td>`
    
                    if (latestrecord != undefined) {
                        boxContainer.insertAdjacentHTML('beforeend', `<div class="column is-5 mb-6"><div class="box"><h5 class="title is-5 has-text-centered">${deviceName}</h5><table class="table is-striped is-fullwidth is-hoverable"><tbody><tr><td>Water Quality</td>${latestrecord['water_status'] == 'clean' ? waterCleanHTML : waterDirtyHTML}</tr><tr><td>Valve Status</td>${latestrecord['valve_status'] == 'on' ? valveOnHTML : valveOffHTML}</tr><tr><td>Location</td><td><span>${location}</span></td></tr><tr><td>Turbidity Records</td><td><a href="${viewRecordsURL}">View Records</a></td></tr></tbody></table></div></div>`)
                    } else {
                        boxContainer.insertAdjacentHTML('beforeend', `<div class="column is-5 mb-6"><div class="box"><h5 class="title is-5 has-text-centered">${deviceName}</h5><table class="table is-striped is-fullwidth is-hoverable"><tbody><tr><td>Water Quality</td><td><span>No records yet.</span></td></tr><tr><td>Valve Status</td><td><input class="toggle" data-id="${deviceID}" type="checkbox"/></td></tr><tr><td>Location</td><td><span>${location}</span></td></tr><tr><td>Turbidity Records</td><td><a href="${viewRecordsURL}">View Records</a></td></tr></tbody></table></div></div>`)
                    }
                }
            } else {
                boxContainer.insertAdjacentHTML('beforeend' , `<div class="column is-5 mb-6"><a href="${addDeviceURL}" class="href"><div class="box box-blank"><div class="content vh-center"><i class="fa fa-plus fa-6x has-text-grey"></i><h2 class="title is-2 has-text-grey">Add Device</h2></div></div></a></div>`)
            }

        });     
    }

    displayDashboard();

});


