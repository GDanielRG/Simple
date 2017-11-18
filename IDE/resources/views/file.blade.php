@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-8 col-md-offset-2">
            <div class="panel panel-default">
                <div class="panel-heading">{{$file->name}}</div>

                <div class="panel-body">
                    <textarea class="codemirror-textarea"></textarea>
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
    </script>
@endsection
