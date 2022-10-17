
// delete device modal
function confirmDeleteDevice(deleteDeviceLink) {

    const deleteModal = document.getElementById('delete-device-modal');
    deleteModal.classList.add('is-active');

    $("#delete-device-modal .is-danger").replaceWith('<button class="button is-danger" onclick="deleteDevice(`' + deleteDeviceLink + '`)">Yes</button>');

}

function deleteDevice(deleteDeviceLink) {
    const fullDeleteURL = window.location.origin + deleteDeviceLink;
    const deleteModal = document.getElementById('delete-device-modal');

    fetch(fullDeleteURL).then((response) => {
        console.log(response);
        deleteModal.classList.remove('is-active');
        location.reload();
    })
}


// delete component modal
function confirmDeleteComponent(deleteComponentLink) {

    const deleteModal = document.getElementById('delete-component-modal');
    deleteModal.classList.add('is-active');

    $("#delete-device-modal .is-danger").replaceWith('<button class="button is-danger" onclick="deleteComponent(`' + deleteComponentLink + '`)">Yes</button>');

}

function deleteComponent(deleteComponentLink) {
    const fullDeleteURL = window.location.origin + deleteComponentLink;
    const deleteModal = document.getElementById('delete-component-modal');

    fetch(fullDeleteURL).then((response) => {
        console.log(response);
        deleteModal.classList.remove('is-active');
    })
}