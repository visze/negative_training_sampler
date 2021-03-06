"""Console script for gtbalancer."""
import sys
import click

from negative_training_sampler.negative_training_balancer import balance_trainingdata

@click.command()
@click.argument("label_file",
                type=click.Path())
@click.argument("genome_file",
                type=click.Path())
@click.option("-o",
              "--output_file",
              default="samples.tsv",
              help="""path to output file; \ndefault:
                      ./[positive, negative]_samples.tsv""")
@click.option("--cores",
              default=1,
              help="""number of used cores\n default: 1""")
@click.option("--memory",
              default="2GB",
              help="""amount of memory per core (e.g. 2 cores * 2GB = 4GB)\ndefault: 2GB""")
def cli(label_file, genome_file, output_file, cores, memory):
    '''
    A simple script that takes a tsv file with positive and negative labels
    and a genome file. Generates negative samples with the same GC distribution
    as the positive samples per chromosome.
    '''

    balance_trainingdata(label_file=label_file,
                         genome_file=genome_file,
                         output_file=output_file,
                         cores=cores,
                         memory_per_core=memory)


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
