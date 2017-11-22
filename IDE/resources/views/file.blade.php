@extends('layouts.app')

@section('content')
<iframe id="video-iframe" width="1" height="1" src="https://www.youtube.com/embed/dskTEpaR_xI?enablejsapi=1" frameborder="0" gesture="media" allowfullscreen></iframe>
<div class="container">
    <div class="row">
        <div class="col-md-12">
            <div class="panel panel-default">
                <div class="panel-heading">{{$file->name}}</div>

                <div class="panel-body">
                    <textarea id="code" class="codemirror-textarea">{{$file->code}}</textarea>
                    <br>
                    <button type="button" onclick="compile()" class="btn btn-info">Run</button>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
            <div class="panel panel-default">
                <p id="output"></p>
            </div>
        </div>
    </div>
</div>
@endsection

@section('scripts')
    <script src="{{ asset('js/codemirror.js') }}"></script>
    <script>
        rate = 0.0
        volume = 0
        var code = $('.codemirror-textarea')[0];
        var editor = CodeMirror.fromTextArea(code, {
            lineNumbers: true
        });

        editor.setSize(null, 900)
        function compile(){
            $.ajax({
                method: 'POST', // Type of response and matches what we said in the route
                url: '/files/{{$file->id}}/compile',
                data: {code: editor.getValue()},
                success: function(response){ // What to do if we succeed
                    toggleVideo('paused')
                    $('#output').text(response)
                },
                error: function(jqXHR, textStatus, errorThrown) { // What to do if we fail
                    document.getElementById('video-iframe').contentWindow.postMessage('{"event":"command","func":"setPlaybackRate","args":[' + rate + ', true]}', '*');
                    document.getElementById('video-iframe').contentWindow.postMessage('{"event":"command","func":"setVolume","args":[' + volume + ', true]}', '*');
                    toggleVideo('play')
                    increase()
                    document.getElementById('video-iframe').contentWindow.postMessage('{"event":"command","func":"setPlaybackRate","args":[' + rate + ', true]}', '*');
                    document.getElementById('video-iframe').contentWindow.postMessage('{"event":"command","func":"setVolume","args":[' + volume + ', true]}', '*');
                    alert(response)
                }
            });
        }
        function toggleVideo(state) {
            if(state == 'paused'){
                document.getElementById('video-iframe').contentWindow.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
                states = 'paused'
            }
            else {
                document.getElementById('video-iframe').contentWindow.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
                states = 'playing'
            }
        }
        function increase(){
            document.getElementById('video-iframe').contentWindow.postMessage('{"event":"command","func":"playVideo","args":""}', '*');            
            if(rate == 1.5){
                rate = 2
                volume = 100
            }
            if(rate == 1.0){
                rate = 1.5
                volume = 80

            }
            if(rate == 0.5)
            {
                rate = 1.0
                volume = 60

            }
            if(rate == 0.25)
            {
                rate = 0.5
                volume = 40

            }
            if(rate == 0.0)
            {
                rate = 0.5
                volume = 20
            }

        }
        $(document).ready(function(){
            states = 'paused'
            toggleVideo('play');            
            document.getElementById('video-iframe').contentWindow.postMessage('{"event":"command","func":"setPlaybackRate","args":[' + rate + ', true]}', '*');
            document.getElementById('video-iframe').contentWindow.postMessage('{"event":"command","func":"setVolume","args":[' + volume + ', true]}', '*');
            toggleVideo('paused');    
            setInterval(function() {
                if(states == "playing")
                    increase()
                    document.getElementById('video-iframe').contentWindow.postMessage('{"event":"command","func":"setPlaybackRate","args":[' + rate + ', true]}', '*');
                    document.getElementById('video-iframe').contentWindow.postMessage('{"event":"command","func":"setVolume","args":[' + volume + ', true]}', '*');
            }, 20000);        
        })
    </script>
@endsection
