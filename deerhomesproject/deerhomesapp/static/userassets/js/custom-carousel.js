$(document).ready(function() {
        var owl = $('.banner-section .owl-carousel');
        owl.owlCarousel({
            margin: 30,
            nav: false,
            loop: true,
            dots: true,
            autoplay: true,
            autoplayTimeout: 4500,
            responsive: {
                0: {
                    items: 1
                },
                576: {
                    items: 1
                },
                768: {
                    items: 1
                },
                992: {
                    items: 1
                }
            }
        })
})

$(document).ready(function() {
    var owl = $('.service-section .owl-carousel');
    owl.owlCarousel({
        margin: 30,
        nav: false,
        loop: true,
        dots: true,
        autoplay: true,
        autoplayTimeout: 4500,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 2.2
            },
            768: {
                items: 2.2
            },
            992: {
                items: 3.2
            },
            1200: {
                items: 3.2
            },
            1440:{
                items: 4.2
            }
        }
    })
})

$(document).ready(function() {
    var owl = $('.testimonial-section .owl-carousel');
    owl.owlCarousel({
        margin: 30,
        nav: false,
        loop: true,
        dots: true,
        autoplay: true,
        autoplayTimeout: 4500,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 1
            },
            992: {
                items: 1
            }
        }
    })
})

$(document).ready(function() {
    var owl = $('.image-section .owl-carousel');
    owl.owlCarousel({
        margin: 10,
        nav: false,
        loop: true,
        dots: true,
        autoplay: true,
        autoplayTimeout: 4500,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 2
            },
            768: {
                items: 3
            },
            992: {
                items: 4
            }
        }
    })
})

$(document).ready(function() {
    var owl = $('.articles-section .owl-carousel');
    owl.owlCarousel({
        margin: 30,
        nav: true,
        loop: true,
        dots: false,
        autoplay: true,
        autoplayTimeout: 4500,
        responsive: {
            0: {
                items: 1
            },
            435: {
                items: 1.6
            },
            576: {
                items: 2
            },
            620: {
                items: 2.3
            },
            715: {
                items: 2.5
            },
            768: {
                items: 2.3
            },
            992: {
                items: 2.5
            },
            1200: {
                items: 2.5
            },
            1300: {
                items: 3.4
            },
            1400: {
                items: 3.5
            },
            1500: {
                items: 3.3
            },
            1620: {
                items: 3.4
            },
            1760:{
                items: 3.6
            }
        }
    })
})