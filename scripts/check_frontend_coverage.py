# Copyright 2020 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Check for decrease in coverage from 100% of frontend files."""

from __future__ import absolute_import  # pylint: disable=import-only-modules
from __future__ import unicode_literals  # pylint: disable=import-only-modules

import os
import re
import sys

import python_utils

LCOV_FILE_PATH = os.path.join(os.pardir, 'karma_coverage_reports', 'lcov.info')
RELEVANT_LCOV_LINE_PREFIXES = ['SF', 'LH', 'LF']

# Contains the name of all files that is not 100% coverage.
# This list must be kept up-to-date; the changes (only remove) should be done
# manually.
# Please keep the list in alphabetical order.
# NOTE TO DEVELOPERS: do not add any new files to this list without asking
# @marianazangrossi first.
NOT_FULLY_COVERED_FILENAMES = [
    'about-page.module.ts',
    'activity-tiles-infinity-grid.directive.ts',
    'admin-config-tab.directive.ts',
    'admin-dev-mode-activities-tab.directive.ts',
    'admin-jobs-tab.directive.ts',
    'admin-misc-tab.directive.ts',
    'admin-navbar.directive.ts',
    'admin-page.directive.ts',
    'admin-prod-mode-activities-tab.directive.ts',
    'admin-roles-tab.directive.ts',
    'alert-message.directive.ts',
    'angular-html-bind.directive.ts',
    'answer-classification.service.ts',
    'answer-details-improvement-task.directive.ts',
    'answer-group-editor.directive.ts',
    'answer-submit-action.directive.ts',
    'App.ts',
    'attribution-guide.directive.ts',
    'audio-bar.directive.ts',
    'audio-file-uploader.directive.ts',
    'audio-player.service.ts',
    'audio-preloader.service.ts',
    'audio-translation-bar.directive.ts',
    'audio-translation-manager.service.ts',
    'autogenerated-audio-player.service.ts',
    'autosave-info-modals.service.ts',
    'background-banner.component.ts',
    'bar-chart.directive.ts',
    'base-content.directive.ts',
    'base-interaction-validation.service.ts',
    'Base.ts',
    'boolean-editor.directive.ts',
    'change-list.service.ts',
    'circular-image.directive.ts',
    'ck-editor-4-rte.directive.ts',
    'ck-editor-4-widgets.initializer.ts',
    'classroom-page.controller.ts',
    'code-repl-prediction.service.ts',
    'code-string-editor.directive.ts',
    'codemirror-mergeview.directive.ts',
    'collection-details-editor.directive.ts',
    'collection-editor-navbar-breadcrumb.directive.ts',
    'collection-editor-navbar.directive.ts',
    'collection-editor-page.directive.ts',
    'collection-editor-state.service.ts',
    'collection-editor-tab.directive.ts',
    'collection-footer.directive.ts',
    'collection-history-tab.directive.ts',
    'collection-local-nav.directive.ts',
    'collection-navbar.directive.ts',
    'collection-node-creator.directive.ts',
    'collection-node-editor.directive.ts',
    'collection-node-list.directive.ts',
    'collection-permissions-card.directive.ts',
    'collection-player-page.directive.ts',
    'collection-settings-tab.directive.ts',
    'collection-statistics-tab.directive.ts',
    'collection-summary-tile.directive.ts',
    'collection-update.service.ts',
    'CollectionNodeObjectFactory.ts',
    'CollectionObjectFactory.ts',
    'CollectionPlaythroughObjectFactory.ts',
    'community-dashboard-page.component.ts',
    'concept-card.directive.ts',
    'ConceptCardObjectFactory.ts',
    'context.service.ts',
    'continue-button.directive.ts',
    'contribution-and-review.service.ts',
    'contribution-opportunities-backend-api.service.ts',
    'contribution-opportunities.service.ts',
    'contributions-and-review.directive.ts',
    'conversation-skin.directive.ts',
    'conversion.ts',
    'convert-to-plain-text.filter.ts',
    'convert-to-plain-text.pipe.ts',
    'coord-two-dim-editor.directive.ts',
    'copier.directive.ts',
    'correctness-footer.directive.ts',
    'create-activity-button.directive.ts',
    'creator-dashboard-page.component.ts',
    'csrf-token.service.ts',
    'current-interaction.service.ts',
    'cyclic-transitions-issue.directive.ts',
    'delete-account-page.component.ts',
    'donate-page.component.ts',
    'drag-and-drop-html-string-editor.directive.ts',
    'drag-and-drop-positive-int-editor.directive.ts',
    'drag-and-drop-sort-input-validation.service.ts',
    'early-quit-issue.directive.ts',
    'editable-collection-backend-api.service.ts',
    'editable-exploration-backend-api.service.ts',
    'editable-story-backend-api.service.ts',
    'editor-navbar-breadcrumb.directive.ts',
    'editor-navigation.directive.ts',
    'email-dashboard-data.service.ts',
    'error-page.component.ts',
    'exploration-automatic-text-to-speech.service.ts',
    'exploration-creation.service.ts',
    'exploration-diff.service.ts',
    'exploration-editor-page.controller.ts',
    'exploration-editor-tab.directive.ts',
    'exploration-embed-button.service.ts',
    'exploration-engine.service.ts',
    'exploration-footer.directive.ts',
    'exploration-graph.directive.ts',
    'exploration-objective-editor.directive.ts',
    'exploration-player-page.controller.ts',
    'exploration-player-state.service.ts',
    'exploration-recommendations.service.ts',
    'exploration-save-and-publish-buttons.directive.ts',
    'exploration-save.service.ts',
    'exploration-states.service.ts',
    'exploration-summary-tile.directive.ts',
    'exploration-title-editor.directive.ts',
    'expression-evaluator.service.ts',
    'expression-interpolation.service.ts',
    'expression-type-parser.service.ts',
    'fatigue-detection.service.ts',
    'feedback-improvement-task.directive.ts',
    'feedback-popup.directive.ts',
    'feedback-tab.directive.ts',
    'FeedbackThreadSummaryObjectFactory.ts',
    'filepath-editor.directive.ts',
    'focus-on.directive.ts',
    'format-timer.filter.ts',
    'fraction-editor.directive.ts',
    'fraction-input-validation.service.ts',
    'generatedParser.ts',
    'google-analytics.initializer.ts',
    'graph-detail.service.ts',
    'graph-editor.directive.ts',
    'graph-input-rules.service.ts',
    'graph-input-validation.service.ts',
    'graph-layout.service.ts',
    'graph-property-editor.directive.ts',
    'graph-viz.directive.ts',
    'hint-and-solution-buttons.directive.ts',
    'hint-and-solution-modal.service.ts',
    'hint-editor.directive.ts',
    'history-tab.directive.ts',
    'html-editor.directive.ts',
    'html-escaper.service.ts',
    'html-select.directive.ts',
    'I18nFooter.ts',
    'image-upload-helper.service.ts',
    'image-uploader.directive.ts',
    'image-with-regions-editor.directive.ts',
    'improvements-tab.directive.ts',
    'input-response-pair.directive.ts',
    'int-editor.directive.ts',
    'item-selection-input-validation.service.ts',
    'language-util.service.ts',
    'lazy-loading.directive.ts',
    'learner-answer-info-card.directive.ts',
    'learner-answer-info.service.ts',
    'learner-dashboard-icons.directive.ts',
    'learner-dashboard-page.controller.ts',
    'learner-local-nav.directive.ts',
    'learner-view-info.directive.ts',
    'learner-view-rating.service.ts',
    'library-footer.directive.ts',
    'library-page.directive.ts',
    'list-of-sets-of-html-strings-editor.directive.ts',
    'list-of-tabs-editor.directive.ts',
    'list-of-unicode-string-editor.directive.ts',
    'loading-dots.directive.ts',
    'logic-demo-test.controller.ts',
    'logic-error-category-editor.directive.ts',
    'logic-question-editor.directive.ts',
    'login-required-message.directive.ts',
    'maintenance-page.controller.ts',
    'math-expression-input-rules.service.ts',
    'math-expression-input-validation.service.ts',
    'math-latex-string-editor.directive.ts',
    'mathjax-bind.directive.ts',
    'messenger.service.ts',
    'misconception-editor.directive.ts',
    'multiple-incorrect-issue.directive.ts',
    'multiple-incorrect-submissions-issue.directive.ts',
    'music-notes-input-rules.service.ts',
    'music-phrase-editor.directive.ts',
    'music-phrase-player.service.ts',
    'nonnegative-int-editor.directive.ts',
    'normalize-whitespace-punctuation-and-case.pipe.ts',
    'normalized-string-editor.directive.ts',
    'number-with-units-editor.directive.ts',
    'number-with-units-validation.service.ts',
    'NumberWithUnitsObjectFactory.ts',
    'numeric-input-validation.service.ts',
    'object-editor.directive.ts',
    'oppia-interactive-code-repl.directive.ts',
    'oppia-interactive-continue.directive.ts',
    'oppia-interactive-drag-and-drop-sort-input.directive.ts',
    'oppia-interactive-end-exploration.directive.ts',
    'oppia-interactive-fraction-input.directive.ts',
    'oppia-interactive-graph-input.directive.ts',
    'oppia-interactive-image-click-input.directive.ts',
    'oppia-interactive-interactive-map.directive.ts',
    'oppia-interactive-item-selection-input.directive.ts',
    'oppia-interactive-logic-proof.directive.ts',
    'oppia-interactive-math-expression-input.directive.ts',
    'oppia-interactive-multiple-choice-input.directive.ts',
    'oppia-interactive-music-notes-input.directive.ts',
    'oppia-interactive-number-with-units.directive.ts',
    'oppia-interactive-numeric-input.directive.ts',
    'oppia-interactive-pencil-code-editor.directive.ts',
    'oppia-interactive-set-input.directive.ts',
    'oppia-interactive-text-input.directive.ts',
    'oppia-noninteractive-collapsible.directive.ts',
    'oppia-noninteractive-image.directive.ts',
    'oppia-noninteractive-link.directive.ts',
    'oppia-noninteractive-math.directive.ts',
    'oppia-noninteractive-skillreview.directive.ts',
    'oppia-noninteractive-tabs.directive.ts',
    'oppia-noninteractive-video.directive.ts',
    'oppia-response-code-repl.directive.ts',
    'oppia-response-continue.directive.ts',
    'oppia-response-drag-and-drop-sort-input.directive.ts',
    'oppia-response-end-exploration.directive.ts',
    'oppia-response-fraction-input.directive.ts',
    'oppia-response-graph-input.directive.ts',
    'oppia-response-image-click-input.directive.ts',
    'oppia-response-interactive-map.directive.ts',
    'oppia-response-item-selection-input.directive.ts',
    'oppia-response-logic-proof.directive.ts',
    'oppia-response-math-expression-input.directive.ts',
    'oppia-response-multiple-choice-input.directive.ts',
    'oppia-response-music-notes-input.directive.ts',
    'oppia-response-number-with-units.directive.ts',
    'oppia-response-numeric-input.directive.ts',
    'oppia-response-pencil-code-editor.directive.ts',
    'oppia-response-set-input.directive.ts',
    'oppia-response-text-input.directive.ts',
    'oppia-short-response-code-repl.directive.ts',
    'oppia-short-response-continue.directive.ts',
    'oppia-short-response-drag-and-drop-sort-input.directive.ts',
    'oppia-short-response-end-exploration.directive.ts',
    'oppia-short-response-fraction-input.directive.ts',
    'oppia-short-response-graph-input.directive.ts',
    'oppia-short-response-image-click-input.directive.ts',
    'oppia-short-response-interactive-map.directive.ts',
    'oppia-short-response-item-selection-input.directive.ts',
    'oppia-short-response-logic-proof.directive.ts',
    'oppia-short-response-math-expression-input.directive.ts',
    'oppia-short-response-multiple-choice-input.directive.ts',
    'oppia-short-response-music-notes-input.directive.ts',
    'oppia-short-response-number-with-units.directive.ts',
    'oppia-short-response-numeric-input.directive.ts',
    'oppia-short-response-pencil-code-editor.directive.ts',
    'oppia-short-response-set-input.directive.ts',
    'oppia-short-response-text-input.directive.ts',
    'oppia-visualization-bar-chart.directive.ts',
    'oppia-visualization-enumerated-frequency-table.directive.ts',
    'oppia-visualization-frequency-table.directive.ts',
    'OppiaFooterDirective.ts',
    'opportunities-list-item.directive.ts',
    'opportunities-list.directive.ts',
    'outcome-destination-editor.directive.ts',
    'outcome-editor.directive.ts',
    'outcome-feedback-editor.directive.ts',
    'param-changes-editor.directive.ts',
    'parameter-name-editor.directive.ts',
    'parameterize-rule-description.filter.ts',
    'pencil-code-editor-validation.service.ts',
    'pie-chart.directive.ts',
    'player-correctness-feedback-enabled.service.ts',
    'player-position.service.ts',
    'player-transcript.service.ts',
    'playthrough-improvement-task.directive.ts',
    'playthrough-issues.directive.ts',
    'playthrough.service.ts',
    'Polyfills.ts',
    'practice-session-page.controller.ts',
    'practice-tab.directive.ts',
    'preferences-page.component.ts',
    'pretest-question-backend-api.service.ts',
    'preview-tab.directive.ts',
    'profile-link-image.directive.ts',
    'profile-link-text.directive.ts',
    'profile-page-navbar.directive.ts',
    'profile-page.component.ts',
    'progress-nav.directive.ts',
    'promo-bar.directive.ts',
    'promo-bar.service.ts',
    'python-program.tokenizer.ts',
    'question-creation.service.ts',
    'question-difficulty-selector.directive.ts',
    'question-editor.directive.ts',
    'question-opportunities.directive.ts',
    'question-player-engine.service.ts',
    'question-player.directive.ts',
    'question-suggestion.service.ts',
    'question-update.service.ts',
    'questions-list.directive.ts',
    'random-selector.directive.ts',
    'rating-display.directive.ts',
    'read-only-collection-backend-api.service.ts',
    'real-editor.directive.ts',
    'RecordedVoiceoversObjectFactory.ts',
    'refresher-exploration-confirmation-modal.service.ts',
    'remove-duplicates-in-array.pipe.ts',
    'request-interceptor.service.ts',
    'response-header.directive.ts',
    'review-material-editor.directive.ts',
    'review-test-page.directive.ts',
    'role-graph.directive.ts',
    'rubrics-editor.directive.ts',
    'rule-editor.directive.ts',
    'rule-type-selector.directive.ts',
    'sanitized-url-editor.directive.ts',
    'schema-based-bool-editor.directive.ts',
    'schema-based-choices-editor.directive.ts',
    'schema-based-custom-editor.directive.ts',
    'schema-based-custom-viewer.directive.ts',
    'schema-based-dict-editor.directive.ts',
    'schema-based-dict-viewer.directive.ts',
    'schema-based-editor.directive.ts',
    'schema-based-expression-editor.directive.ts',
    'schema-based-float-editor.directive.ts',
    'schema-based-html-editor.directive.ts',
    'schema-based-html-viewer.directive.ts',
    'schema-based-int-editor.directive.ts',
    'schema-based-list-editor.directive.ts',
    'schema-based-list-viewer.directive.ts',
    'schema-based-primitive-viewer.directive.ts',
    'schema-based-unicode-editor.directive.ts',
    'schema-based-unicode-viewer.directive.ts',
    'schema-based-viewer.directive.ts',
    'score-ring.directive.ts',
    'search-bar.directive.ts',
    'search-results.directive.ts',
    'select2-dropdown.directive.ts',
    'set-of-html-string-editor.directive.ts',
    'set-of-unicode-string-editor.directive.ts',
    'settings-tab.directive.ts',
    'shared.ts',
    'sharing-links.directive.ts',
    'side-navigation-bar.directive.ts',
    'signup-page.component.ts',
    'skill-concept-card-editor.directive.ts',
    'skill-creation.service.ts',
    'skill-description-editor.directive.ts',
    'skill-editor-main-tab.directive.ts',
    'skill-editor-navbar-breadcrumb.directive.ts',
    'skill-editor-navbar.directive.ts',
    'skill-editor-page.controller.ts',
    'skill-editor-state.service.ts',
    'skill-mastery.directive.ts',
    'skill-misconceptions-editor.directive.ts',
    'skill-prerequisite-skills-editor.directive.ts',
    'skill-questions-tab.directive.ts',
    'skill-rubrics-editor.directive.ts',
    'skill-selector-editor.directive.ts',
    'skill-selector.directive.ts',
    'skill-update.service.ts',
    'SkillDifficultyObjectFactory.ts',
    'SkillObjectFactory.ts',
    'skills-list.directive.ts',
    'skills-mastery-list.directive.ts',
    'social-buttons.directive.ts',
    'solution-editor.directive.ts',
    'solution-explanation-editor.directive.ts',
    'state-content-editor.directive.ts',
    'state-editor.directive.ts',
    'state-editor.service.ts',
    'state-graph-visualization.directive.ts',
    'state-hints-editor.directive.ts',
    'state-improvement-suggestion.service.ts',
    'state-interaction-editor.directive.ts',
    'state-name-editor.directive.ts',
    'state-param-changes-editor.directive.ts',
    'state-property.service.ts',
    'state-responses.directive.ts',
    'state-solution-editor.directive.ts',
    'state-top-answers-stats.service.ts',
    'state-translation-editor.directive.ts',
    'state-translation-status-graph.directive.ts',
    'state-translation.directive.ts',
    'state-tutorial-first-time.service.ts',
    'StateCardObjectFactory.ts',
    'StatesObjectFactory.ts',
    'statistics-tab.directive.ts',
    'stats-reporting.service.ts',
    'story-creation.service.ts',
    'story-editor-navbar-breadcrumb.directive.ts',
    'story-editor-navbar.directive.ts',
    'story-editor-page.controller.ts',
    'story-editor-state.service.ts',
    'story-editor.directive.ts',
    'story-node-editor.directive.ts',
    'story-summary-tile.directive.ts',
    'story-update.service.ts',
    'story-viewer-backend-api.service.ts',
    'story-viewer-navbar-breadcrumb.directive.ts',
    'story-viewer-page.directive.ts',
    'StoryContentsObjectFactory.ts',
    'StoryNodeObjectFactory.ts',
    'student.ts',
    'subtopic-summary-tile.directive.ts',
    'subtopic-viewer-navbar-breadcrumb.directive.ts',
    'subtopic-viewer-page.controller.ts',
    'SubtopicObjectFactory.ts',
    'SubtopicPageObjectFactory.ts',
    'subtopics-list-tab.directive.ts',
    'subtopics-list.directive.ts',
    'suggestion-improvement-task.directive.ts',
    'suggestion-modal-for-exploration-editor.service.ts',
    'suggestion-modal-for-exploration-player.service.ts',
    'suggestion-modal-for-learner-dashboard.service.ts',
    'summary-list-header.directive.ts',
    'supplemental-card.directive.ts',
    'svm-prediction.service.ts',
    'teacher.ts',
    'teacher2.ts',
    'test-interaction-panel.directive.ts',
    'thanks-page.component.ts',
    'thread-table.directive.ts',
    'thumbnail-uploader.directive.ts',
    'top-navigation-bar.directive.ts',
    'topic-creation.service.ts',
    'topic-editor-navbar-breadcrumb.directive.ts',
    'topic-editor-navbar.directive.ts',
    'topic-editor-page.controller.ts',
    'topic-editor-routing.service.ts',
    'topic-editor-state.service.ts',
    'topic-editor-stories-list.directive.ts',
    'topic-editor-tab.directive.ts',
    'topic-questions-tab.directive.ts',
    'topic-selector.directive.ts',
    'topic-summary-tile.directive.ts',
    'topic-update.service.ts',
    'topic-viewer-navbar-breadcrumb.directive.ts',
    'topic-viewer-page.controller.ts',
    'topic-viewer-stories-list.directive.ts',
    'TopicObjectFactory.ts',
    'topics-and-skills-dashboard-backend-api.service.ts',
    'topics-and-skills-dashboard-navbar-breadcrumb.directive.ts',
    'topics-and-skills-dashboard-navbar.directive.ts',
    'topics-and-skills-dashboard-page.controller.ts',
    'topics-list.directive.ts',
    'training-panel.directive.ts',
    'translate-text.service.ts',
    'translation-file-hash-loader.service.ts',
    'translation-opportunities.directive.ts',
    'translation-tab.directive.ts',
    'translator-overview.directive.ts',
    'truncate-and-capitalize.filter.ts',
    'truncate-and-capitalize.pipe.ts',
    'truncate-input-based-on-interaction-answer-type.filter.ts',
    'truncate.filter.ts',
    'truncate.pipe.ts',
    'tutor-card.directive.ts',
    'unicode-string-editor.directive.ts',
    'unresolved-answers-overview.directive.ts',
    'url-interpolation.service.ts',
    'utils.service.ts',
    'value-generator-editor.directive.ts',
    'version-diff-visualization.directive.ts',
    'version-tree.service.ts',
    'voiceover-opportunities.directive.ts',
    'voiceover-recording.service.ts',
    'warnings-and-alerts.directive.ts',
    'worked-example-editor.directive.ts',
]


class LcovStanzaRelevantLines(python_utils.OBJECT):
    """Gets the relevant lines from a lcov stanza."""

    def __init__(self, stanza):
        """Initialize the object which provides relevant data of a lcov
        stanza in order to calculate any decrease in frontend test coverage.

        Args:
            stanza: list(str). Contains all the lines from a lcov stanza.

        Raises:
            Exception: file_path is empty.
            Exception: Total lines number is not found.
            Exception: Covered lines number is not found.
        """

        match = re.search('SF:(.+)\n', stanza)
        if match is None:
            raise Exception(
                'The test path is empty or null. '
                'It\'s not possible to diff the test coverage correctly.')
        _, file_name = os.path.split(match.group(1))
        self.file_name = file_name

        match = re.search(r'LF:(\d+)\n', stanza)
        if match is None:
            raise Exception(
                'It wasn\'t possible to get the total lines of {} file.'
                'It\'s not possible to diff the test coverage correctly.'
                .format(file_name))
        self.total_lines = int(match.group(1))

        match = re.search(r'LH:(\d+)\n', stanza)
        if match is None:
            raise Exception(
                'It wasn\'t possible to get the covered lines of {} file.'
                'It\'s not possible to diff the test coverage correctly.'
                .format(file_name))
        self.covered_lines = int(match.group(1))


def get_stanzas_from_lcov_file():
    """Get all stanzas from a lcov file. The lcov file gather all the frontend
    files that has tests and each one has the following structure:
    TN: test name
    SF: file path
    FNF: total functions
    FNH: functions covered
    LF: total lines
    LH: lines covered
    BRF: total branches
    BRH: branches covered
    end_of_record

    Returns:
        list(LcovStanzaRelevantLines). A list with all stanzas.
    """
    f = python_utils.open_file(LCOV_FILE_PATH, 'r')
    lcov_items_list = f.read().split('end_of_record')
    stanzas_list = []

    for item in lcov_items_list:
        if item.strip('\n'):
            stanza = LcovStanzaRelevantLines(item)
            stanzas_list.append(stanza)

    return stanzas_list


def check_not_fully_covered_filenames_list_is_sorted():
    """Check if NOT_FULLY_COVERED_FILENAMES list is in alphabetical order."""
    if NOT_FULLY_COVERED_FILENAMES != sorted(
            NOT_FULLY_COVERED_FILENAMES, key=lambda s: s.lower()):
        sys.exit(
            'The \033[1mNOT_FULLY_COVERED_FILENAMES\033[0m list must be'
            ' kept in alphabetical order.')


def check_coverage_changes():
    """Checks if the blacklist for not fully covered files needs to be changed
    by:
    - File renaming
    - File deletion

    Raises:
        Exception: LCOV_FILE_PATH doesn't exist.
    """
    if not os.path.exists(LCOV_FILE_PATH):
        raise Exception(
            'Expected lcov file to be available at {}, but the'
            ' file does not exist.'.format(LCOV_FILE_PATH))

    stanzas = get_stanzas_from_lcov_file()
    remaining_blacklisted_files = list(NOT_FULLY_COVERED_FILENAMES)
    errors = ''

    for stanza in stanzas:
        file_name = stanza.file_name
        total_lines = stanza.total_lines
        covered_lines = stanza.covered_lines

        if file_name not in remaining_blacklisted_files:
            if total_lines != covered_lines:
                errors += (
                    '\033[1m{}\033[0m seems to be not completely tested.'
                    ' Make sure it\'s fully covered.\n'.format(file_name))
        else:
            if total_lines == covered_lines:
                errors += (
                    '\033[1m{}\033[0m seems to be fully covered!'
                    ' Before removing it manually from the blacklist'
                    ' in the file'
                    ' scripts/check_frontend_test_coverage.py, please'
                    ' make sure you\'ve followed the unit tests rules'
                    ' correctly on:'
                    ' https://github.com/oppia/oppia/wiki/Frontend'
                    '-unit-tests-guide#rules\n'.format(file_name))

            remaining_blacklisted_files.remove(file_name)

    if remaining_blacklisted_files:
        for test_name in remaining_blacklisted_files:
            errors += (
                '\033[1m{}\033[0m is in the frontend test coverage'
                ' blacklist but it doesn\'t exist anymore. If you have'
                ' renamed it, please make sure to remove the old file'
                ' name and add the new file name in the blacklist in'
                ' the file scripts/check_frontend_test_coverage.py.\n'
                .format(test_name))

    if errors:
        python_utils.PRINT('------------------------------------')
        python_utils.PRINT('Frontend Coverage Checks Not Passed.')
        python_utils.PRINT('------------------------------------')
        sys.exit(errors)
    else:
        python_utils.PRINT('------------------------------------')
        python_utils.PRINT('All Frontend Coverage Checks Passed.')
        python_utils.PRINT('------------------------------------')

    check_not_fully_covered_filenames_list_is_sorted()


def main():
    """Runs all the steps for checking if there is any decrease of 100% covered
    files in the frontend.
    """
    check_coverage_changes()


# The 'no coverage' pragma is used as this line is un-testable. This is because
# it will only be called when check_frontend_coverage.py is used as a script.
if __name__ == '__main__': # pragma: no cover
    main()