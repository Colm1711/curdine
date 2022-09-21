/* Function to close Booststrap alert after 3 seconds*/
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);


/* Function to display Map location */
function initMap() {
    var location = {
        lat: 39.7817213,
        lng: -89.6501481
    };
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: location,
        streetViewControl: false,
    });
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
}

/*  Function for Order form to validate if item is not selected raise an alert 
    Opens Modal if successful.
*/
function valthis() {
    var checkBoxes = document.getElementsByClassName( 'form-check-input');
    var isChecked = false;
    
    
        for (var i = 0; i < checkBoxes.length; i++) {
            if ( checkBoxes[i].checked ) {
                isChecked = true;
            };
        };
        if ( isChecked ) {
            $("#exampleModal").modal('show');
            } else {
                $('.alert').removeClass('d-none').addClass('show');
            }   
    }

/* Submits Order form in Modal */    
function form_submit() {
        document.getElementById("sectionForm").submit();
       }    