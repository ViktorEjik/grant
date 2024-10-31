<?php

namespace MediaWiki\Search;

use MediaWiki\Category\Category;
use MediaWiki\Parser\ParserOutput;
use MediaWiki\Title\Title;

/**
 * Extracts data from ParserOutput for indexing in the search engine.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 * http://www.gnu.org/copyleft/gpl.html
 *
 * @since 1.28
 */
class ParserOutputSearchDataExtractor {

	/**
	 * Get a list of categories, as an array with title text strings.
	 *
	 * @param ParserOutput $parserOutput
	 * @return string[]
	 */
	public function getCategories( ParserOutput $parserOutput ) {
		$categories = [];

		foreach ( $parserOutput->getCategoryNames() as $key ) {
			$name = Category::newFromName( $key )->getName();
			$categories[] = str_replace( '_', ' ', $name );
		}

		return $categories;
	}

	/**
	 * Get a list of external links from ParserOutput, as an array of strings.
	 *
	 * @param ParserOutput $parserOutput
	 * @return string[]
	 */
	public function getExternalLinks( ParserOutput $parserOutput ) {
		return array_keys( $parserOutput->getExternalLinks() );
	}

	/**
	 * Get a list of outgoing wiki links (including interwiki links), as
	 * an array of prefixed title strings.
	 *
	 * @param ParserOutput $parserOutput
	 * @return string[]
	 */
	public function getOutgoingLinks( ParserOutput $parserOutput ) {
		$outgoingLinks = [];

		foreach ( $parserOutput->getLinks() as $linkedNamespace => $namespaceLinks ) {
			foreach ( $namespaceLinks as $linkedDbKey => $_ ) {
				$outgoingLinks[] =
					Title::makeTitle( $linkedNamespace, $linkedDbKey )->getPrefixedDBkey();
			}
		}

		return $outgoingLinks;
	}

	/**
	 * Get a list of templates used in the ParserOutput content, as prefixed title strings
	 *
	 * @param ParserOutput $parserOutput
	 * @return string[]
	 */
	public function getTemplates( ParserOutput $parserOutput ) {
		$templates = [];

		foreach ( $parserOutput->getTemplates() as $tNS => $templatesInNS ) {
			foreach ( $templatesInNS as $tDbKey => $_ ) {
				$templateTitle = Title::makeTitle( $tNS, $tDbKey );
				$templates[] = $templateTitle->getPrefixedText();
			}
		}

		return $templates;
	}

}
