
$(document).ready(function() {
    app.initialize();
});

var app = {
    // Application Constructor
    initialize: function() {

        $('#app').append('<div id="buttonGroup1" class="app btn-group-vertical">');
        $('#buttonGroup1').append('<button id="inspectionsBtn" class="btn btn-default btn-large" type="button">Inspections</button>');
        $('#buttonGroup1').append('<button id="settingsBtn" class="btn btn-default btn-large" type="button">Settings</button>');
        $('#inspectionsBtn').on('click', app.sections.inspection);
    },

    clearApp: function() {
        $('#app').empty();
    },

    topNavigation: function() {
        $('#app').append('<div id="topNav" class="navbar navbar-fixed-top navbar-inverse">');
        $('#topNav').append('<a class="navbar-brand" href="#">Title</a>');
        $('#topNav').append('<ul id="navBar" class="nav navbar-nav">');
        $('#navBar').append('<li class="active"><a href="#">Home</a></li>');
        $('#navBar').append('<li><a href="#">Link</a></li>');
        $('#navBar').append('<li><a href="#">Link</a></li>');
    },

    sections: {
        inspection: function() {
            app.clearApp();
            app.topNavigation();
            
            $('#app').append('<div id="inspectionGroup" class="input-group"  style="margin-top:50px;">');
            $('#inspectionGroup').append('<span class="input-group-addon"><input id="section1CheckBox" type="checkbox"></span>');
            $('#inspectionGroup').append('<div class="sectionHeader"><h4>Hoist</h4></div>');
            $('#app').append('<div id="section1" class="well"><div id="section1Select"></div></div>');

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

            // app.buildControls();
        }
    },

    toggleSection: function( event ) {
        console.log('toggle');
        var section = String(event.data.section);
        $('#' + section).slideToggle();
    },

    buildControls: function(){

        var sections = app.inspectionDefinition.sections;

        for (section in sections) {
            console.log(section);
        }
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
    ],

    inspectionDefinition: {
        main: {
            customerName: 'Customer Name',
            shipToAddress: 'Ship To Address',
            serviceWO: 'Service WO',
            date: 'Date',
            specificLocation: 'Specific Location',
            manufacturer: 'Manufacturer',
            type: 'Type',
            modelNumber: 'Model Number',
            capacit: 'Capacity'
        },
        sections: {
            hoist: {
                lowerSheavesSprockets: 'Lower Sheaves / Sprockets',
                lowerSheavesSprocketBearings: 'Lower Sheaves / Sprocket Bearings',
                blockThrustBearings: 'Block Thrust Bearings',
                hook: 'Hook',
                hookLatch: 'Hook Latch',
                upperSheavesSprockets: 'Upper Sheaves / Sprockets',
                upperSheavesSprocketBearings: 'Upper Sheaves / Sprocket Bearings',
                idlerSheaveSprocket: 'Idler Sheave / Sprocket',
                ropeChain: 'Rope / Chain',
                ropeChainTerminations: 'Rope / Chain Terminations',
                ropeGuideThroatsOpening: 'Rope Guide / Throats Opening',
                ropeDrum: 'Rope Drum',
                drumBearing: 'Drum Bearing',
                drumBullGear: 'Drum Bull Gear',
                gearBoxGears: 'Gear Box Gears',
                gearBoxBearingsSeals: 'Gear Box Bearings & Seals',
                brakes: 'Brakes',
                brakeLinings: 'Brake Linings',
                hoistStructureConnections: 'Hoist Structure / Connections',
                motorCouplings: 'Motor Couplings',
                motor: 'Motor',
                controlLimits: 'Control Limits',
                powerOverloadLimits: 'Power / Overload Limits'
            },
            trolley: {
                driveWheels: 'Drive Wheels',
                trailerWheels: 'Trailer Wheels',
                wheelGearing: 'Wheel Gearing',
                pinions: 'Pinions',
                gearBoxGears: 'Gear Box Gears',
                gearBoxBearingsSeals: 'Gear Box Bearings & Seals',
                brakes: 'Brakes',
                brakeLinings: 'Brake Linings',
                couplings: 'Couplings',
                motors: 'Motors',
                trolleyStructureConnections: 'Trolley Structure / Connections'
            },
            bridge: {
                driveWheels: 'Drive Wheels',
                trailerWheels: 'Trailer Wheels',
                wheelGearing: 'Wheel Gearing',
                pinions: 'Pinions',
                gearBoxGears: 'Gear Box Gears',
                gearBoxBearingsSeals: 'Gear Box Bearings & Seals',
                brakes: 'Brakes',
                brakeLinings: 'Brake Linings',
                couplings: 'Couplings',
                motors: 'Motors',
                bridgeStructureGirder: 'Bridge Structure - Girder',
                bridgeStructureEndTrucks: 'Bridge Structure - End Trucks',
                bridgeStructureConnections: 'Bridge Structure - Connections',
                walkway: 'Walkway'
            },
            runway: {
                runwayRailRailFasteners: 'Runway Rail / Rail Fasteners',
                runwayStructureConnections: 'Runway Structure / Connections',
                endStops: 'End Stops'
            },
            electrics: {
                mainCollectors: 'Main Collectors',
                trolleyConductors: 'Trolley Conductors',
                pendantStationRadioControls: 'Pendant Station / Radio Controls',
                pendantCable: 'Pendant Cable',
                cabControls: 'Cab Controls',
                emergencyStopButton: 'Emergency Stop Button',
                panelsJunctionBoxes: 'Panels / Junction Boxes',
                climateControl: 'Climate Control',
                lights: 'Lights',
                magnetControls: 'Magnet Controls',
                wiringCondition: 'Wiring Condition',
                mainlineContactor: 'Mainline Contactor',
                contactorsVfds: 'Contactors / Vfds',
                timers: 'Timers',
                resistors: 'Resistors'
            },
            general: {
                capacitySignsPresent: 'Capacity Signs Present',
                cleanliness: 'Cleanliness',
                lubrication: 'Lubrication',
                safetyGuardsCovers: 'Safety Guards / Covers',
                limitSwichOperation: 'Limit Swich Operation',
                safetyAccess: 'Safety Access',
                others: 'Others',
                documentation: 'Documentation'
            }
        }
    }

};
