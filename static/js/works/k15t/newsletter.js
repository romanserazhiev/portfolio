$(function() {
  newNewsletterSignUp();
  // preventing from scrolling up when clicking on the Submit button
  $('.k15t-subscribe-button').on('click', function(e) {
    e.preventDefault();
  })
});


function newNewsletterSignUp () {
  var $newsletterBanner = $('.animated-newsletter-sign-up-full');

  if (!$newsletterBanner.length || !$newsletterBanner.is(':visible')) {
      return false;
  }

  const $newsletterBannerWrapper = $('.animated-newsletter-sign-up', $newsletterBanner);
  let oldBannerOpacity = 1;
  let flag = true;


  $(document).on('scroll', $newsletterBanner, function () {
      const scrollBarPosition = $(document).scrollTop();
      const windowHeight = $(window).height();
      const bannerTopPosition = $newsletterBanner.offset().top - windowHeight;
      const bannerHeight = $newsletterBanner.height();
      let bannerBottomPosition = bannerHeight + bannerTopPosition;
      let bannerOpacity = 1;
      let p;
      let bannerInTheMiddle = $newsletterBanner.offset().top - (windowHeight/2) + (bannerHeight/2);
      let approxBannerInTheMiddle = Math.floor(bannerInTheMiddle)

      if (bannerHeight > windowHeight) {
          bannerBottomPosition = (bannerTopPosition + windowHeight) - (windowHeight / 4);
      }

      if (scrollBarPosition > bannerTopPosition) {
          p = (scrollBarPosition - bannerTopPosition) * 100 / (bannerBottomPosition - bannerTopPosition);
          bannerOpacity = (100 - p) / 100;

          if (bannerOpacity < 0) {
              bannerOpacity = 0;
          }
      }

      if (bannerOpacity !== oldBannerOpacity) {
          const startScale = 0.9;
          oldBannerOpacity = bannerOpacity;
          p = (100 - (100 * bannerOpacity)) / 100;

          const opacity = Math.abs(bannerOpacity - 1);
          let scale = (1 - startScale) * p + startScale;

          if (scale > 1) {
              scale = 1;
          }

          $newsletterBannerWrapper.css({
              'opacity': opacity,
              '-webkit-transform': 'scale(' + scale + ')',
              'transform': 'scale(' + scale + ')'
          });
      }
  });
}