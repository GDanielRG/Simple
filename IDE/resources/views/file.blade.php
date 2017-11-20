@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-12">
            <div class="panel panel-default">
                <div class="panel-heading">{{$file->name}}</div>

                <div class="panel-body">
                    <textarea id="code" class="codemirror-textarea">{{$file->code}}</textarea>
                    <br>
                    <button type="button" onclick="compile()" class="btn btn-info">Compile</button>
                    <button type="button" onclick="compileRun()" class="btn btn-primary">Compile and run</button>
                    <button type="button" onclick="save()" class="btn btn-success">Save</button>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection

@section('scripts')
    <script src="{{ asset('js/codemirror.js') }}"></script>
    <script>
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
                    alert(response)
                },
                error: function(jqXHR, textStatus, errorThrown) { // What to do if we fail
                    alert(response)
                }
            });
        }
    </script>
@endsection
