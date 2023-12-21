$(document).ready(function() {
                $.ajax({
                    type: "GET",
                    url: "/get_states/", // Replace with the actual server-side script
                    dataType: "json",
                    success:  function (data) {
            var obj = JSON.parse(data);
            $count=1
            for ($i = 0; $i <= obj.length+1; $i++) {
                $("#state").append("<option value='" + obj[$i].fields.state + "' >" + obj[$i].fields.state + "</option>");
            }
        }, error: function (d1) {
            console.log(d1)
        }
                });


        function fetchCities(state) {
                $.ajax({
                    type: "GET",
                    url: "/get_cities/", // Replace with your server-side script
                    data: { 'state': state },
                    dataType: "json",
                    success:  function (data) {
                                $("#city").empty();
            var obj = JSON.parse(data);
            $count=1
            for ($i = 0; $i <= obj.length+1; $i++) {
                $("#city").append("<option value='" + obj[$i].fields.city  + "' >" + obj[$i].fields.city + "</option>");
            }
        }, error: function (d1) {
            console.log(d1)
        }
                });
        }

            // Event handler for state selection change
            $("#state").on("change", function() {
                var selectedState = $(this).val();
                fetchCities(selectedState);
            });

            // Initialize the city dropdown based on the default state
            fetchCities($("#state").val());



    function fetchofficers(city) {
    console.log("Fetching officers for city:", city);
                $.ajax({
                    type: "GET",
                    url: "/get_officers/", // Replace with your server-side script
                    data: { 'city': city },
                    dataType: "json",
                    success:  function (data) {
                                $("#officers").empty();
            var obj = JSON.parse(data);
            $count=1
            for ($i = 0; $i <= obj.length+1; $i++) {
                $("#officers").append($("<option>" + obj[$i].fields.name + "</option>").attr("value", obj[$i].pk));
            }
        }, error: function (d1) {
            console.log(d1)
        }
                });
        }


            $("#city").on("change", function() {
                var selectedCity = $(this).val();
                console.log("Selected city:", selectedCity);
                fetchofficers(selectedCity);
            });


            // Initialize the city dropdown based on the default state
            fetchofficers($("#city").val());


        });