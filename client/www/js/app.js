
$(document).ready(function() {
    app.initialize();
});

var app = {
    // Application Constructor
    initialize: function() {

        $('#app').append('<div id="mainMenuGroup" class="app btn-group-vertical">');
        $('#mainMenuGroup').append('<button id="inspectionsBtn" class="btn btn-large">Inspections</button>');
        $('#mainMenuGroup').append('<button id="settingsBtn" class="btn btn-large">Settings</button>');
        $('#inspectionsBtn').on('click', app.sections.inspection.create);
    },

    clearApp: function() {
        $('#app').empty();
    },

    topNavigation: function() {
        $('#app').append('<div id="navigationBar" class="navbar navbar-inverse">');
        $('#navigationBar').append('<a class="navbar-brand" href="#">CSS</a>');
        $('#navigationBar').append('<ul id="navigationBarList" class="nav navbar-nav">');
        $('#navigationBarList').append('<li class="active"><a href="#">Home</a></li>');
        $('#navigationBarList').append('<li><a href="#">Link</a></li>');
        $('#navigationBarList').append('<li><a href="#">Link</a></li>');
    },

    sections: {

        inspection: {

            create: function() {
                app.clearApp();
                app.topNavigation();
                $('#app').append('<div id="spacer" style="margin-top:50px;">');
                app.sections.inspection.buildNewInspection();
            },

            buildNewInspection: function(){

                
                app.sections.inspection.buildMainSection();

                $('#app').append('<div id="sectionWrapper" class="col-12 col-lg-12"></div>')
                var sectionWrapper = $('#sectionWrapper');
                var sections = app.inspectionDefinition.sections;
                
                

                for (var section in sections) {

                    var groupId = section + 'Group'
                    var checkBoxId = section + 'CheckBox';
                    var wellId = section + 'Well';

                    // Sections
                    sectionWrapper.append('<div id="' + groupId + '" class="input-group">');
                    $('#' + groupId).append('<span class="input-group-addon"><input id="' + checkBoxId + '" type="checkbox"></span>');
                    $('#' + groupId).append('<div class="sectionHeader"><h4>' + section + '</h4></div>');
                    sectionWrapper.append('<div id="' + wellId + '" class="well collapse in"></div>');
                    $('#' + checkBoxId).on('change', {'wellId': wellId, 'section': section}, app.sections.inspection.toggleWell);
                    $('#' + wellId).slideToggle();
                }
            },

            buildMainSection: function() {

                var mainItems = app.inspectionDefinition.main;

                var customerName = app.sections.inspection.buildInputGroup('customerName');
                var shipToAddress = app.sections.inspection.buildInputGroup('shipToAddress');
                var serviceWO = app.sections.inspection.buildInputGroup('serviceWO');
                var date = app.sections.inspection.buildInputGroup('date');
                var specificLocation = app.sections.inspection.buildInputGroup('specificLocation');
                var manufacturer = app.sections.inspection.buildInputGroup('manufacturer');
                var type = app.sections.inspection.buildInputGroup('type');
                var modelNumber = app.sections.inspection.buildInputGroup('modelNumber');
                var capacit = app.sections.inspection.buildInputGroup('capacit');

                $('#app').append(
                    $('<div class="col-12 col-lg-12"></div>').append(
                        $('<div class="col-lg-5 input-group">' + $(customerName).html() + '</div>')
                    ).append(
                        $('<div class="col-lg-1"></div>')
                    ).append(
                        $('<div class="col-lg-5 input-group">' + $(shipToAddress).html() + '</div>')
                    )
                );

                $('#app').append(
                    $('<div class="col-12 col-lg-12"></div>').append(
                        $('<div class="col-lg-5 input-group">' + $(customerName).html() + '</div>')
                    ).append(
                        $('<div class="col-lg-1"></div>')
                    ).append(
                        $('<div class="col-lg-5 input-group">' + $(shipToAddress).html() + '</div>')
                    )
                );

                

                // $('#app').append('<div id="mainSection"></div>')

                // var mainSectionObj = $('#mainSection');

                // for (var item in mainItems) {

                //     var itemInput = item + 'Input';
                //     var label = app.inspectionDefinition.main[item];
                //     // Main
                //     mainSectionObj.append('<div class="input-group"><span class="input-group-addon">' + label + '</span><input type="text" class="form-control" id="' + itemInput + '" placeholder="' + label + '"></div>');
                // }
            },

            buildInputGroup: function( item ) {
                var itemInput = item + 'Input';
                var label = app.inspectionDefinition.main[item];
                return $('<div><span class="input-group-addon">' + label + '</span><input type="text" class="form-control" id="' + itemInput + '" placeholder="' + label + '"></div>');
            },

            toggleWell: function( event ) {
                
                var wellId = String(event.data.wellId);
                var section = String(event.data.section);
                var wellObj = $('#' + wellId)

                // Create the ddSlick only if it hasn't been created yet.
                if ($('#' + wellId + ' .dd-container').size() == 0) {
                    
                    for (var subsection in app.inspectionDefinition.sections[section]) {
                        var ddSlickId = subsection + 'DdSlick';
                        
                        wellObj.append('<div id="' + ddSlickId + '"></div>')

                        var ddData = [
                            {
                                text: subsection,
                                value: 0,
                                selected: true,
                                description: ""
                            },
                            {
                                text: subsection,
                                value: 1,
                                selected: false,
                                description: "Pass",
                                imageSrc: "http://dl.dropbox.com/u/40036711/Images/facebook-icon-32.png"
                            },
                            {
                                text: subsection,
                                value: 2,
                                selected: false,
                                description: "Fail",
                                imageSrc: "http://dl.dropbox.com/u/40036711/Images/twitter-icon-32.png"
                            },
                            {
                                text: subsection,
                                value: 3,
                                selected: false,
                                description: "Not applicable",
                                imageSrc: "http://dl.dropbox.com/u/40036711/Images/linkedin-icon-32.png"
                            },
                            {
                                text: subsection,
                                value: 4,
                                selected: false,
                                description: "Dash",
                                imageSrc: "http://dl.dropbox.com/u/40036711/Images/foursquare-icon-32.png"
                            }
                        ];

                        // Create the ddSlick thingy
                        $('#' + ddSlickId).ddslick({
                            data: ddData,
                            width: 300,
                            imagePosition: "right",
                            selectText: subsection,
                            showSelectedHTML: true,
                            onSelected: function (data) {
                                //console.log(data);
                            }
                        });
                    }
                }

                $('#' + wellId).slideToggle();
            }
        }
    },

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
