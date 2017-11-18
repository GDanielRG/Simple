@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-8 col-md-offset-2">
            <div class="panel panel-default">
                <div class="panel-heading">My files</div>

                <div class="panel-body">
                    @foreach($files as $file)
                        <a href="/files/{{$file->id}}"><div class="alert alert-success">
                            {{ $file->name }}
                        </div></a>
                    @endforeach
                </div>
            </div>
        </div>
    </div>
</div>
@endsection