/*
Copyright (c) 2003-2012, CKSource - Frederico Knabben. All rights reserved.
For licensing, see LICENSE.html or http://ckeditor.com/license
*/

CKEDITOR.editorConfig = function( config )
{
	// Define changes to default configuration here. For example:
	config.language = 'zh-cn';

  config.toolbar = 'MyToolbar';

  config.toolbar_MyToolbar = [
    { name: 'document', items : [ 'NewPage','Preview' ] },
    { name: 'clipboard', items : [ 'Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo' ] },
    { name: 'editing', items : [ 'Find','Replace','-','SelectAll','-','Scayt' ] },
    { name: 'insert', items : [ 'Image','Table','HorizontalRule','PageBreak' ] },
    '/',
    { name: 'styles', items : [ 'Styles','Format' ] },
    { name: 'basicstyles', items : [ 'Bold','Italic','Strike','-','RemoveFormat' ] },
    { name: 'paragraph', items : [ 'NumberedList','BulletedList','-','Outdent','Indent','-','Blockquote' ] },
    { name: 'links', items : [ 'Link','Unlink','Anchor' ] },
    { name: 'tools', items : [ 'Maximize' ] }
  ];
};
