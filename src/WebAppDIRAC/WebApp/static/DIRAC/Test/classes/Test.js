Ext.define('DIRAC.Test.classes.Test', {
    extend : 'Ext.dirac.core.Module',
    requires :['Ext.grid.*',
               'Ext.data.*',
               'Ext.util.*',
               'Ext.state.*'],
    initComponent:function(){
      var me = this;

      me.launcher.title = "CE availability monitoring";
      me.launcher.maximized = false;
    
      me.launcher.width = 520;
      me.launcher.height = 254;
    
      me.launcher.x = 0;
      me.launcher.y = 0;
    
      Ext.apply(me, {
        layout : 'border',
        bodyBorder : false,
        defaults : {
          collapsible : true,
          split : true
        }
      });
    
      me.callParent(arguments);
    },

    buildUI:function(){
      function colorerBold(val) {
        if (val == 'Success') {
            return '<span style="color:green;"><b>' + val + '</b></span>';
        } else {
            return '<span style="color:red;"><b>Fail</b></span>';
        }
        return val;
      }
      function colorer(val) {
        if (val == 'Success') {
            return '<span style="color:green;">' + val + '</span>';
        } else if (val =='runned_failed') {
            return '<span style="color:red;">Fail</span>';
        }
        return val;
      }
      var me = this;

      me.dataStore = new Ext.data.JsonStore({

        proxy : {
            type : 'ajax',
            url : GLOBAL.BASE_URL + 'Test/getData',
            reader : {
                type : 'json',
                root : 'result'
            },
            timeout : 50000
        },
        fields : [{name : 'site', type : 'string' },
                  {name : 'service', type: 'string'},
                  {name : 'test', type: 'string'},
                  {name : 'result', type: 'string'},
                  {name : 'description', type: 'string'}],
        autoLoad : true,
        pageSize : 20,

    });

      me.grid = Ext.create('Ext.grid.Panel', {
        region : 'center',
        store : me.dataStore,
        header : false,
        columns : [{
            header : 'Site',
            sortable : true,
            dataIndex : 'site',
            align : 'left'
        },
        {
            header : 'Service',
            sortable : true,
            dataIndex : 'service',
            align : 'left'
        },
        {
            header : 'Test',
            sortable : true,
            dataIndex : 'test',
            align : 'left'
        },
        {
            header : 'Result',
            sortable : true,
            dataIndex : 'result',
            align : 'right',
            renderer : colorerBold
        },
        {
            header : 'Description',
            sortable : true,
            dataIndex : 'description',
            align : 'right'
        }]
        //{
        //    header : 'OldStatus',
        //    sortable : true,
        //    dataIndex : 'old_status',
        //    align : 'right',
        //    renderer : colorer
        //}]
        
    });

     me.add([me.grid]);
    
    }
});
