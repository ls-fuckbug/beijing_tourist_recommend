"use strict";
if(typeof Placeholdem === 'function') {
	if (document.querySelectorAll( '[placeholder]' ).length) {
		Placeholdem( document.querySelectorAll( '[placeholder]' ) );
	};
}

function pieChart() {
	//circle progress bar
	if ((jQuery().easyPieChart) && (jQuery.support.leadingWhitespace)) {
		var count = 0 ;
		//var colors = ['#fbcf61', '#e6557c', '#00c1e4'];
		var colors = ['#4cddf3'];
		jQuery('.chart').each(function(){
				
			var imagePos = jQuery(this).offset().top;
			var topOfWindow = jQuery(window).scrollTop();
			if (imagePos < topOfWindow+600) {

				jQuery(this).easyPieChart({
			        barColor: colors[count],
					trackColor: '#ffffff',
					scaleColor: false,
					scaleLength: false,
					lineCap: 'butt',
					lineWidth: 10,
					size: 180,
					rotate: 0,
					animate: 2000,
					onStep: function(from, to, percent) {
							jQuery(this.el).find('.percent').text(Math.round(percent));
						}
			    });
			}
			count++;
			if (count >= colors.length) { count = 0};
		});
	}
}

jQuery(document).ready(function() {

	//animation to elements on scroll
	if (jQuery().appear) {
		jQuery('.to_animate').appear().css({opacity: 0});
		//console.log(jQuery('.to_animate').filter(':appeared'));
		jQuery('.to_animate').filter(':appeared').each(function(index){
			var self = jQuery(this);
			var animationClass = !self.data('animation') ? 'fadeInUp' : self.data('animation');
			var animationDelay = !self.data('delay') ? 200 : self.data('delay');
			setTimeout(function(){
				self.addClass("animated " + animationClass);
			}, index * animationDelay);
		});

		jQuery('body').on('appear', '.to_animate', function(e, $affected ) {
			jQuery($affected).each(function(index){
				var self = jQuery(this);
				var animationClass = !self.data('animation') ? 'fadeInUp' : self.data('animation');
				var animationDelay = !self.data('delay') ? 200 : self.data('delay');
				setTimeout(function(){
					self.addClass("animated " + animationClass);
				}, index * animationDelay);
			});
		});
	}

	//counters init on scroll
	if (jQuery().appear) {
		jQuery('.counter').appear();
		jQuery('body').on('appear', '.counter', function(e, $affected ) {
			jQuery($affected).each(function(index){
				if (jQuery(this).hasClass('counted')) {
					return;
				} else {
					jQuery(this).countTo().addClass('counted');
				}
				
			});
		});
	}

	//menu
	if (jQuery().superfish) {
		jQuery('ul.sf-menu').superfish({
			delay:       700,
			animation:   {opacity:'show',height:'show'},
			//animation:   {opacity:'show'},
			animationOut: {opacity: 'hide'},
			speed:       'fast',
			disableHI:   false,
			cssArrows:   false,
			autoArrows:  false
		});
	}

	//toTop
	if (jQuery().UItoTop) {
        jQuery().UItoTop({ easingType: 'easeOutQuart' });
    }

    //horizontal accordion
    if (jQuery().elastislide) {
	    jQuery('#carousel').elastislide({
	        // imageW : 260,
	        // border : 0,
	        minItems : 2,
	        // margin : 30
	        orientation : 'vertical'
	    });
	}

	//parallax
	if (jQuery().parallax) {
		jQuery('#testimonials').parallax("50%", 0.1);
		//jQuery('#footer').parallax("50%", 0.2);
	}

	
	//funny text
	if (jQuery().funnyText) {
		jQuery('.funnyText').funnyText({
			speed: 700,
			borderColor: 'transparent',
			activeColor: '#E07850',
			color: '#fff',
			fontSize: '2.4em',
			direction: 'both'
		});
	}

    //prettyPhoto
    if (jQuery().prettyPhoto) {
     jQuery("a[data-gal^='prettyPhoto']").prettyPhoto({
      hook: 'data-gal',
   theme: 'facebook' /* light_rounded / dark_rounded / light_square / dark_square / facebook / pp_default*/
    });
    }

   	//carousel
   	if (jQuery().carousel) {
		jQuery('.carousel').carousel();
	}

	//owl carousel
	if (jQuery().owlCarousel) {
		//upcomming events carousel
	    jQuery(".owl-carousel.owl-items-5").owlCarousel({
	    	navigation : true,
	    	navigationText : false,
	    	pagination : false,
	    	items: 5
	    });
	    //team carousel
	    jQuery(".owl-carousel.team").owlCarousel({
	    	navigation : true,
	    	navigationText : false,
	    	pagination : false,
	    	items: 4,
	    	// itemsDesktop: 3,
	    	// itemsDesktopSmall: 2,
	    	// itemsTablet: 2
	    });
	    //partners
	    jQuery(".partners").owlCarousel({
	    	navigation : true,
	    	navigationText : false,
	    	pagination : false,
	    	items: 5,
	    	autoPlay: 5000
	    });
	}
    
    //nice scroll
	// if (jQuery().niceScroll) {
 //    	jQuery("html").niceScroll({
 //    		cursorcolor: '#ac000b',
 //    		cursorborder: 'none',
 //    		cursorborderradius: '1',
 //    		cursorwidth: '6px'
 //    	});
	// }

	//bx slider
	if (jQuery().bxSlider) {
		jQuery('.bxslider').bxSlider({
			auto: true,
			controls: false,
			pager: false,
		  	mode: 'fade'
		});

		jQuery('.vertical-slider').bxSlider({
			mode: 'vertical',
			//slideWidth: 300,
			minSlides: 2,
			slideMargin: 30,
			pager: false
		});
	}

	//timeline
	if (jQuery().timelinr) {
		if(jQuery('#timeline').length) {
			jQuery('#timeline').timelinr({
				orientation: 	'vertical',
				issuesSpeed: 	300,
				datesSpeed: 	100,
				arrowKeys: 		'true',
			});
		}
	}

	//single page localscroll and scrollspy
	var navHeight = jQuery('#header').outerHeight(true) + 40;
	jQuery('body').scrollspy({
		target: '.mainmenu_wrap',
		offset: navHeight
	});
	if (jQuery().localScroll) {
		jQuery('#mainmenu, #land').localScroll({
			duration:1900,
			easing:'easeOutQuart',
			offset: 0
		});
		
	}

	//portfolio and horizontal slider animation
	jQuery('.portfolio_links').find('a').css({opacity: 0});
	jQuery('.isotope-item, .horizontal_slider_introimg, .portfolio_item_image').hover(
	 	function() {
			jQuery( this ).find('.portfolio_links a').stop().animate({ opacity: 1}, 50, 'easeOutExpo').parent().find('.p-view').toggleClass('moveFromLeft').end().find('.p-link').toggleClass('moveFromRight');
		}, function() {
			jQuery( this ).find('.portfolio_links a').stop().animate({ opacity: 0}, 50, 'easeOutExpo').parent().find('.p-view').toggleClass('moveFromLeft').end().find('.p-link').toggleClass('moveFromRight');
		}
	);

	//teaser style5 animation
	jQuery('.single_teaser.icons.style5').hover(
	 	function() {
			jQuery( this ).find('i').addClass('moveFromLeft').end().find('h3').addClass('moveFromRight').end().find('p').addClass('moveFromBottom');
		}, function() {
			jQuery( this ).find('i').removeClass('moveFromLeft').end().find('h3').removeClass('moveFromRight').end().find('p').removeClass('moveFromBottom');
		}
	);


	//twitter
	//slide tweets
	jQuery('#tweets .twitter').bind('loaded', function(){
		jQuery(this).addClass('flexslider').find('ul').addClass('slides');
	});
	if (jQuery().tweet) {
		jQuery('.twitter').tweet({
			modpath: "./twitter/",
		    count: 3,
		    avatar_size: 48,
		    loading_text: 'loading twitter feed...',
		    join_text: 'auto',
		    username: 'ThemeForest', 
		    template: "{avatar}{time}{join}<span class=\"tweet_text\">{tweet_text}</span>"
		});
	}

	//land slider
	jQuery('#land')
			.find('.land').css({'opacity': 0})
			.end()
			.find('.shown')
			.css({'opacity': 1});


});

jQuery(window).load(function(){
	
	//init gallery
	Grid.init();

	//chart
	pieChart();

	//land slider
	jQuery('.main-tab a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
		var newSlideId = jQuery(this).attr('class');
		var oldSlideId = e.relatedTarget.getAttribute('class');
		jQuery('#land')
			.find('#'+oldSlideId)
			.animate({opacity: 0}, {queue: false})
			.removeClass('shown')
			.addClass('not_shown')
			.end()
			.find('#'+newSlideId)
			.removeClass('not_shown')
			.addClass('shown')
			.animate({opacity: 1}, {queue: false})
	});



	//bxSlider
	// if (jQuery().bxSlider) {
	// 	jQuery('.bxslider').bxSlider({
	// 		//pagerCustom: '#bx-pager'
	// 	});
	// }
	
	setTimeout(function(){
		jQuery('.progress-bar').addClass('stretchRight');
	}, 600);

	//stick header to top
	if (jQuery().sticky) {
	    jQuery("#header").sticky({ 
	    		topSpacing: 0,
	    		scrollBeforeStick: 10
	    	},
	    	function(){ 
	    		jQuery("#header").stop().animate({opacity:0}, 0).delay(500).stop().animate({opacity:1}, 800);
	    	},
	       	function(){ 
	    		jQuery("#header").stop().animate({opacity:0}, 0).delay(800).stop().animate({opacity:1}, 1000);
	    	}
	    );
	}
	

	if (jQuery().flexslider) {
		
		jQuery(".flexslider").flexslider({
			animation: "fade",
			useCSS: true,
			controlNav: true,   
			directionNav: false,
		    prevText: "",
		    nextText: "",
			//animationLoop: false,
			smoothHeight: true,
			slideshowSpeed:5000,
			animationSpeed:800,
			after :function( slider ){
				//console.log(slider.find('.slide_description').children());
			  	//bg-color1 - class for #mainslider
			  	//var currentClass = $mainSlider.find('.flex-active-slide').attr('data-bg');
			  	//$mainSlider.attr('class', currentClass);
			}
		});
	}

	jQuery('body').delay(1000).scrollspy('refresh');


	//preloader
	jQuery(".preloaderimg").fadeOut();
	jQuery(".preloader").delay(200).fadeOut("slow").delay(200, function(){
		jQuery(this).remove();
	});

	//fractionslider
	// if (jQuery().fractionSlider) {
	// 	var $mainSlider = jQuery('#mainslider');
	// 	jQuery('.slider').fractionSlider({
	// 		'fullWidth': 			true,
	// 		'controls': 			false, 
	// 		'pager': 				true,
	// 		'responsive': 			true,
	// 		'dimensions': 			"1920,700",
	// 	    'increase': 			true,
	// 		'pauseOnHover': 		false,
	// 		'slideEndAnimation': 	true,
	// 		'timeout' : 			3000,
	// 		'speedOut' : 			1000
	// 		//'slideTransitionSpeed' :500,

	// 	});
	// }



	//flickr
	// use http://idgettr.com/ to find your ID
	if (jQuery().jflickrfeed) {
		jQuery("#flickr").jflickrfeed({
			flickrbase: "http://api.flickr.com/services/feeds/",
			limit: 6,
			qstrings: {
				id: "63512867@N07"
			},
			itemTemplate: '<a href="{{image_b}}" rel="prettyPhoto[pp_gal]"><li><img alt="{{title}}" src="{{image_s}}" /></li></a>'
		}, function(data) {
			jQuery("#flickr a").prettyPhoto({
				theme: 'facebook'
	   		});
	   		jQuery("#flickr li").hover(function () {						 
			   jQuery(this).find("img").stop().animate({ opacity: 0.5 }, 200);
		    }, function() {
			   jQuery(this).find("img").stop().animate({ opacity: 1.0 }, 400);
		    });
		});
	}

	//animation to elements
	// var windowHeight = jQuery(window).height();
	// jQuery('.to_fade, .block-header, .block-header + p').each(function(){
	// var imagePos = jQuery(this).offset().top;
	// var topOfWindow = jQuery(window).scrollTop();
	// 	if (imagePos < topOfWindow+windowHeight-100) {
	// 		jQuery(this).addClass("animated fadeInUp");
	// 	}
	// });

	// jQuery('.to_slide_left').each(function(){
	// var imagePos = jQuery(this).offset().top;

	// var topOfWindow = jQuery(window).scrollTop();
	// 	if (imagePos < topOfWindow+windowHeight-100) {
	// 		jQuery(this).addClass("animated fadeInLeft");
	// 	}
	// });

	// jQuery('.to_slide_right').each(function(){
	// var imagePos = jQuery(this).offset().top;

	// var topOfWindow = jQuery(window).scrollTop();
	// 	if (imagePos < topOfWindow+windowHeight-100) {
	// 		jQuery(this).addClass("animated fadeInRight");
	// 	}
	// });

	//flexslider
	// jQuery(".slides").find("li").each(function(){
	// 	var h = jQuery(this).height();
	// 	var childH = jQuery(this).find(".leftcontent_wrap").actual("height");
	// 	var childRH = jQuery(this).find(".rightcontent_wrap").actual("height");
	// 	var childD = jQuery(this).find(".slide_description").actual("height");
	// 	var padding = (h / 2) - (childH / 2);
	// 	var paddingR = (h / 2) - (childRH / 2);
	// 	var topD = ((h / 2) - ((childD / 2) ));
	// 	jQuery(this).find(".leftcontent_wrap").css("padding-top" , padding);
	// 	jQuery(this).find(".rightcontent_wrap").css("padding-top" , paddingR);
	// 	jQuery(this).find(".slide_description").css("top" , topD);
	// });

	

});

jQuery(window).resize(function(){
	if (jQuery().sticky) {
		jQuery("#header").sticky('update');
	}
	jQuery('body').scrollspy('refresh');

	//flexslider
	// jQuery(".slides").find("li").each(function(){
	// 	var h = jQuery(this).height();
	// 	var childH = jQuery(this).find(".leftcontent_wrap").actual("height");
	// 	var childRH = jQuery(this).find(".rightcontent_wrap").actual("height");
	// 	var childD = jQuery(this).find(".slide_description").actual("height");
	// 	var padding = (h / 2) - (childH / 2);
	// 	var paddingR = (h / 2) - (childRH / 2);
	// 	var topD = ((h / 2) - ((childD / 2) ));
	// 	jQuery(this).find(".leftcontent_wrap").css("padding-top" , padding);
	// 	jQuery(this).find(".rightcontent_wrap").css("padding-top" , paddingR);
	// 	jQuery(this).find(".slide_description").css("top" , topD);
	// });

});

jQuery(window).scroll(function() {

	//circle progress bar
	pieChart();


});