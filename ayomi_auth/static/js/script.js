   $(document).ready(function () {
            $("#update-email").submit(function (event) {
                $.ajax({
                    type: "POST",
                    beforeSend: function (request) {
                        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
                        request.setRequestHeader("X-CSRFToken", csrftoken);
                    },
                    url: $("#update-email").attr("action"),
                    data: {
                        'email': $('#new-email').val(),

                    },
                    success: function (response) {
                        console.log("submitted");
                        console.log(response)
                        $("#email").text(response['email'])
                    }
                });
                return false;
            });

        });