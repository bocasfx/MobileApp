
$(document).ready(function() {
    app.initialize();
});

var app = {
    // Application Constructor
    initialize: function() {
        $('#inspectionsBtn').on('click', {'section': 'inspections'}, app.navigate);

        // Inspections
        $('#section1Select').ddslick({
            data: app.ddData,
            width: 300,
            imagePosition: "right",
            selectText: "Select your favorite social network",
            onSelected: function (data) {
                console.log(data);
            }
        });
        $('#section1').slideToggle();
        $('#section1CheckBox').on('change', {'section': 'section1'}, app.toggleSection);
        console.log('App init done.');
    },

    navigate: function( event ) {
        var section = event.data.section;
        window.location = String(section) + '.html';
    },

    toggleSection: function( event ) {
        console.log('toggle');
        var section = String(event.data.section);
        $('#' + section).slideToggle();
    },

    ddData: [
        {
            text: "Facebook",
            value: 1,
            selected: false,
            description: "Description with Facebook",
            imageSrc: "http://dl.dropbox.com/u/40036711/Images/facebook-icon-32.png"
        },
        {
            text: "Twitter",
            value: 2,
            selected: false,
            description: "Description with Twitter",
            imageSrc: "http://dl.dropbox.com/u/40036711/Images/twitter-icon-32.png"
        },
        {
            text: "LinkedIn",
            value: 3,
            selected: true,
            description: "Description with LinkedIn",
            imageSrc: "http://dl.dropbox.com/u/40036711/Images/linkedin-icon-32.png"
        },
        {
            text: "Foursquare",
            value: 4,
            selected: false,
            description: "Description with Foursquare",
            imageSrc: "http://dl.dropbox.com/u/40036711/Images/foursquare-icon-32.png"
        }
    ]


};
