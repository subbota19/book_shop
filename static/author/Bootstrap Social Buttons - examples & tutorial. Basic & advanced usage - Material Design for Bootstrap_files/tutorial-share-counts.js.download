jQuery(document).ready(function() {

  getFbCount();

  function getFbCount() {

    var url = "https://mdbootstrap.com/wp-content/themes/mdbootstrap4/inc/get_social_counts.php?thisurl=" + window.location.href.split('?')[0];
    var oldShareCounts = parseInt(shareCountsData.oldShareCounts);

    jQuery.ajax({
      url: url,
      method: "GET"
    })
      .done(function(response) {
  
        if( isNaN(oldShareCounts) ) {
  
          oldShareCounts = 0;
        }

        response = JSON.parse( response );

        var count = response.share_count;

        if( count === false ) {

          return;
        }
  
        count += oldShareCounts > 0 ? oldShareCounts : 0;
  
        if (+count >= 10) {
  
          jQuery("#fb-share-count").text(count);
        } else {
  
          jQuery("#fb-share-count").remove();
        }
      })
      .fail(function(error) {

        console.error(error);
      });
  }
});