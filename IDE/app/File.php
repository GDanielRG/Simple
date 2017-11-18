<?php

namespace App;

use App\User;
use Illuminate\Database\Eloquent\Model;

class File extends Model
{
    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name', 'code',
    ];

    public function user()
    {
        return $this->belongsTo(User::class);
    }
}
