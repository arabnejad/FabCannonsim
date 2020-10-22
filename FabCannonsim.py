
from base.fab import *

# Add local script and template path for FabSim3
add_local_paths("FabCannonsim")


@task
@load_plugin_env_vars("FabCannonsim")
def Cannonsim(app,
              label='',
              **args):
    '''
    Submit a single job of Cannon_app

    fabsim <remote_machine> Cannonsim:cannon_app
    fabsim localhost Cannonsim:cannon_app
    '''
    if len(label) > 0:
        env.job_name_template += "_{}".format(label)

    update_environment(args)
    with_config(app)
    execute(put_configs, app)
    job(dict(script='cannonsim'), args)


@task
@load_plugin_env_vars("FabCannonsim")
def Cannonsim_ensemble(app,
                       label='',
                       **args):
    '''
    Submit an ensemble of canon_app jobs

    fabsim <remote_machine> Cannonsim_ensemble:cannon_app
    fabsim localhost Cannonsim_ensemble:cannon_app
    '''

    if len(label) > 0:
        env.job_name_template += "_{}".format(label)

    update_environment(args)
    sweep_dir = find_config_file_path(app) + "/SWEEP"
    env.script = 'cannonsim'
    run_ensemble(app, sweep_dir, **args)
